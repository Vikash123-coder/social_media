# Generated by Django 4.1 on 2022-09-28 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0016_alter_profile_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='profile.jpg', upload_to='profiles'),
        ),
    ]
