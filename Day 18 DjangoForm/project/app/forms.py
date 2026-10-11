from django import forms
from app.models import *

class ProductForm(forms.ModelForm):
    class Meta:
        model = ProductModel
        field = '__all_'
        exclude = ['phone']
