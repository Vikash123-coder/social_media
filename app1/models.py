from distutils.command.upload import upload
from email.policy import default
from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User

# Create your models here.  
    
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    following = models.ManyToManyField(User, related_name = 'following', blank=True)
    image = models.ImageField(upload_to = 'profiles', default='profile.jpg')
    updated = models.DateField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    
    def profiles_posts(self):
        return self.post_set.all()
    def __str__(self):
        return str(self.user.username) 

    class Meta:
        ordering = ('-created',)    