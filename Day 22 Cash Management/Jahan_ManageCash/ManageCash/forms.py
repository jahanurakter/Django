from django import forms
from ManageCash.models import *
from django.contrib.auth.forms import UserCreationForm

class UserForm(UserCreationForm):
    class Meta:
        model = UserModel
        fields = '__all__'
