

from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm
class signUpForm(UserCreationForm):
    class Meta:
        model = User
        fields  = ['username', 'first_name', 'last_name', 'email']
        labels  = {'email':'Valid Email'}
        
