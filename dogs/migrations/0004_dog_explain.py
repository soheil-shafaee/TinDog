# Generated by Django 4.1.5 on 2023-06-02 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dogs', '0003_dog_dog_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='dog',
            name='explain',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
