# Generated by Django 4.1 on 2022-09-20 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_rename_post_userpost_rename_cation_userpost_caption'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userpost',
            name='image',
            field=models.ImageField(upload_to='app1/static/images'),
        ),
    ]
