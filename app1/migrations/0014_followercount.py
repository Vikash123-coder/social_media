# Generated by Django 4.1 on 2022-09-23 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0013_userpost_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='followerCount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('follower', models.CharField(max_length=100)),
                ('user', models.CharField(max_length=100)),
            ],
        ),
    ]
