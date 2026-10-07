from django import forms
from django.contrib.auth.forms import UserCreationForm
from form_app.models import *
class RegisterForm(UserCreationForm):
    class Meta:
         model = UserModel
         fields = [ 'username','full_name', 'user_type', 'email', 'password1', 'password2']

class CategoryForm(forms.ModelForm):
     class Meta:
          model = CategoryModel
          fields = ['name']