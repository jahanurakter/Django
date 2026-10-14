from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from purchases.models import *


class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email', 'password1', 'password2']

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfileModel
        fields = '__all__'
        exclude = ['user']



