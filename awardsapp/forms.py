from .models import Profile, Project, Vote
from django import forms 
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class SignUpForm(UserCreationForm):    
    email = forms.EmailField(max_length=254, help_text='Required. Input a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2') 

class CreateProfileForm(ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']

class AddProjectForm(ModelForm):
    class Meta:
        model = Project
        exclude = ['profile', 'post_date', 'voters', 'design_score','usability_score','content_score','average_design','average_usability','average_content','average_score']

class RateProjectForm(ModelForm):
    class Meta:
        model = Vote
        exclude = ['post_date', 'voter', 'project'] 

