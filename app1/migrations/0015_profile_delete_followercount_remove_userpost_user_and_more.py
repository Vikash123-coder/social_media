# Generated by Django 4.1 on 2022-09-26 10:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app1', '0014_followercount'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated', models.DateField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('following', models.ManyToManyField(blank=True, related_name='following', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-created',),
            },
        ),
        migrations.DeleteModel(
            name='followerCount',
        ),
        migrations.RemoveField(
            model_name='userpost',
            name='user',
        ),
        migrations.DeleteModel(
            name='userporfile',
        ),
        migrations.DeleteModel(
            name='userPost',
        ),
    ]