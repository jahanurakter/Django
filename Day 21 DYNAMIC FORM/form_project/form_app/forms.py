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

class ProductForm (forms.ModelForm):
     class Meta:
          model = ProductModel
          fields = '__all__'
          exclude = ['created_by', 'total_amount']

          widgets={
               'expired_date':forms.DateInput(attrs={'type':'date'}),
               'product_name':forms.TextInput(attrs={'placeholder':'Enter Product Name'}),
               'description':forms.TextInput(attrs={'placeholder':'Enter Product Description'}),

          }
