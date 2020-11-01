from django.forms import ModelForm
from .models import Projects, Profile
from django.contrib.auth.forms import UserCreationForm
from django.contrib .auth.models import User
from django import forms
from pyuploadcare.dj.forms import ImageField

class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class NewProjectForm(forms.ModelForm):
    class Meta:
        model = Projects
        exclude = ['Owner', 'pub_date', 'owner_profile']
        widgets = {
          'project_description': forms.Textarea(attrs={'rows':6, 'cols':6,}),
        }
        

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']
        widgets = {
          'bio': forms.Textarea(attrs={'rows':2, 'cols':10,}),
        }
        
        


