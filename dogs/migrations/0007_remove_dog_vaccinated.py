# Generated by Django 4.1.5 on 2023-06-07 16:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dogs', '0006_alter_dog_gender_alter_dog_vaccinated'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dog',
            name='vaccinated',
        ),
    ]
