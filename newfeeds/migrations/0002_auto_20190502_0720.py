# Generated by Django 2.1.7 on 2019-05-02 07:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newfeeds', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dog',
            name='dog_color',
        ),
        migrations.DeleteModel(
            name='Dog',
        ),
        migrations.DeleteModel(
            name='DogColor',
        ),
    ]
