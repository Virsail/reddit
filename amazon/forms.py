from django.forms import ModelForm
#from .models import Event 
from django.contrib.auth.forms import UserCreationForm
from django.contrib .auth.models import User
from django import forms
from pyuploadcare.dj.forms import ImageField

class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

