from django.contrib.auth.models import User
from django import forms
from CalorieCounter_ap.models import *
from django.contrib.auth.forms import UserCreationForm

class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']

class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfileModel
        fields= '__all__'
        exclude = ['user','bmr']

class ConsumeCalorieForm(forms.ModelForm):
    class Meta:
        model = ConsumedCalorieModel
        fields = '__all__'
        exclude = ['user']
        
