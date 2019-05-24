# Generated by Django 2.2.1 on 2019-05-23 17:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Breed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('breed_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='DogColor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color_name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='default.jpg', upload_to='profile_img')),
                ('owner_phone', models.CharField(default='08x-xxx-xxxx', max_length=20)),
                ('owner_address', models.TextField(default='default Address')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='DogFound',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('founder_name', models.CharField(max_length=255)),
                ('founder_info', models.TextField()),
                ('founder_phone', models.CharField(max_length=20)),
                ('dog_gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], default='Male', max_length=10)),
                ('dog_image', models.ImageField(default='default-dog.jpg', upload_to='dog_img')),
                ('dog_breed', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='accounts.Breed')),
                ('dog_color', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='accounts.DogColor')),
            ],
        ),
        migrations.CreateModel(
            name='Dog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dog_name', models.CharField(max_length=50)),
                ('dog_gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], default='Male', max_length=10)),
                ('dog_dob', models.DateField(blank=True, null=True)),
                ('dog_info', models.TextField(default='-')),
                ('dog_age', models.IntegerField(default=0)),
                ('dog_image', models.ImageField(default='default-dog.jpg', upload_to='dog_img')),
                ('qr_code', models.TextField(default='-')),
                ('dog_status', models.CharField(choices=[('Death', 'Death'), ('Normal', 'Normal'), ('Lost', 'Lost')], default='Normal', max_length=20)),
                ('color1', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='accounts.DogColor')),
                ('dog_breed', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='accounts.Breed')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
