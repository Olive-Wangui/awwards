from django import forms
from django.contrib.auth.models import User
from .models import *

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    bio = forms.CharField()
    
    class Meta:
        model = User
        fields = ['username', 'email']
        
class ProfileUpdateForms(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image', 'bio']

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        exclude = ['author', 'profile', 'likes', 'comments']
        
        