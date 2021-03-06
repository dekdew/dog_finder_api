from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User


# Create your views here.
from accounts.forms import UserRegisterForms, UserUpdateForms, ProfileUpdateForm, DogRegisterForms
from accounts.models import Breed, Dog, DogColor
from generate_QR import qrcode


def register(req):
    if req.method == 'POST':
        form = UserRegisterForms(req.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(req, f'Account created for {username}')

            new_user = authenticate(username=form.cleaned_data['username'],
                                    password=form.cleaned_data['password1'],
                                    )
            login(req, new_user)

            return redirect('edit_profile')
    else:
        form = UserRegisterForms()

    return render(req, 'accounts/register.html', {'form': form})


@login_required
def register_dog(req):
    if req.method == 'POST':
        print(req.user.profile)
        dog_form = DogRegisterForms(req.POST, req.FILES)

        if dog_form.is_valid():
            dog = dog_form.save(commit=False)
            dog.owner = req.user
            breed = Breed.objects.filter(breed_name=dog_form.cleaned_data.get('dog_breed'))
            print(breed)
            dog.breed = breed
            dog_form.save()
            qrcode(dog.id)

            return redirect('view_dog', dog_id=dog.id)
    else:
        dog_form = DogRegisterForms()
    context = {'dog_form': dog_form}
    return render(req, 'accounts/dog_register.html', context)


def my_login(req):
    context = {}
    if req.method == 'POST':
        username = req.POST.get('username')
        password = req.POST.get('password')

        user = authenticate(req, username=username, password=password)

        if user:
            login(req, user)
            next_url = req.POST.get('next_url')
            if next_url:
                return redirect(next_url)
            return redirect('my_profile')
        else:
            context['username'] = username
            context['password'] = password
            context['error'] = 'Wrong Username or Password'

    next_url = req.GET.get('next')
    if next_url:
        context['next_url'] = next_url
    return render(req, 'accounts/login.html', context)


def my_logout(req):
    logout(req)
    return redirect('index')


@login_required
def edit_profile(req):
    if req.method == 'POST':
        user_form = UserUpdateForms(req.POST, instance=req.user)
        profile_form = ProfileUpdateForm(req.POST, req.FILES, instance=req.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(req, f'Your account has been update!')
            return redirect('my_profile')
    else:
        user_form = UserUpdateForms(instance=req.user)
        profile_form = ProfileUpdateForm(instance=req.user.profile)
        storage = messages.get_messages(req)
        storage.used = True

    context = {
        'user_form': user_form,
        'profile_form': profile_form
    }
    return render(req, 'accounts/edit-profile.html', context=context)


@login_required
def my_profile(req):
    context = {}
    user = req.user
    if req.method == 'POST':
        pass
    else:
        dog_list = Dog.objects.filter(owner=user)
        context['dog_list'] = dog_list

    return render(req, 'accounts/my-profile.html', context=context)


def view_dog(req, dog_id):
    dog = Dog.objects.get(pk=dog_id)
    context = {
        'dog': dog,
        'dog_id': str(dog.id)
    }
    return render(req, 'accounts/view-dog.html', context=context)


def view_profile(req, profile_id):
    user = User.objects.get(pk=profile_id)
    context = {
        'user_profile': user
    }
    return render(req, 'accounts/view-profile.html', context=context)


@login_required
def edit_dog(req, dog_id):
    dog = Dog.objects.get(id=dog_id)
    if req.user.id == dog.owner.id:
        if req.method == 'POST':
            form = DogRegisterForms(req.POST, instance=dog)
            if form.is_valid():
                form.save()
                messages.success(req, f'Your dog has been update!')
                return redirect('my_profile')
        else:
            form = DogRegisterForms(instance=dog)
            storage = messages.get_messages(req)
            storage.used = True

        context = {
            'form': form,
            'dog_id': dog_id
        }
        return render(req, 'accounts/edit-dog.html', context=context)
    else:
        return redirect('login')


@login_required
def delete_dog(req, dog_id):
    dog = Dog.objects.get(id=dog_id)
    if req.user.id == dog.owner.id:
        dog.delete()
        return redirect('my_profile')
    else:
        return redirect('login')
