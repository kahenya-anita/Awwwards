from .models import Profile
from django import forms 

class CreateProfileForm(ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']