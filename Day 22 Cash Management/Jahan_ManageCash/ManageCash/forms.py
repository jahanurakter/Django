from django import forms
from ManageCash.models import *
from django.contrib.auth.forms import UserCreationForm

class UserForm(UserCreationForm):
    class Meta:
        model = UserModel
        fields = ['username','email','password1','password2']

class AddCashForm(forms.ModelForm):
    class Meta:
        model = AddCashModel
        fields = '__all__'
        exclude = ['cash_name']

class ExpenseForm(forms.ModelForm):
    class Meta:
        model = ExpenseModel
        fields = '__all__'
        exclude = ['expense_name']

        widgets = {
            'datetime':forms.DateInput(attrs={'type':'date'})
        }
