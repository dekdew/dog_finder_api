# Generated by Django 2.1.7 on 2019-05-06 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newfeeds', '0006_auto_20190505_0301'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post_status',
            field=models.CharField(choices=[('0', '0'), ('1', '1')], max_length=2),
        ),
        migrations.AlterField(
            model_name='post',
            name='types',
            field=models.CharField(choices=[('0', '0'), ('1', '1')], max_length=2),
        ),
    ]