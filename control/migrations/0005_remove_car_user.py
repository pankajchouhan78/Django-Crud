# Generated by Django 3.2.16 on 2023-06-03 10:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('control', '0004_car_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car',
            name='user',
        ),
    ]