# Generated by Django 4.1.5 on 2023-06-02 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dogs', '0002_rename_dogs_dog'),
    ]

    operations = [
        migrations.AddField(
            model_name='dog',
            name='dog_photo',
            field=models.ImageField(default=1, upload_to='dogs_photo/'),
            preserve_default=False,
        ),
    ]
