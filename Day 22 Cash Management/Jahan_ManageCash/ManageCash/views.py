from django.shortcuts import render,redirect,get_list_or_404
from django.contrib.auth.decorators import login_required
from ManageCash.models import *
from ManageCash.forms import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm

def dashboard_view(req):
    return render(req, 'dashboard.html')

def login_view(req):
    form_data=AuthenticationForm()
    if req.method == 'POST':
        form_data=AuthenticationForm(req, data=req.POST)
        if form_data.is_valid():
            user=form_data.get_user()
            if user:
                login(req, user)
                return redirect('login_view')

        context={
            'form_data':form_data,
            'page_title':'login',
            'head_title': 'Log in Your Account',
            'btn_title': 'Login',

        }
    return render(req, 'login.html',context)

def register_view(req):
    form_data=UserForm()
    if req.method == 'POST':
        form_data=UserForm(req.POST)
        if form_data.is_valid():
            form_data.save()
            return redirect('login_view')
        context={
            'form_data':form_data,
            'page_title':'Register Your Account',
            'btn_title': 'Register',
        
            }
            
    return render(req, 'master/base-form.html',context)

def logout_view(req):
    logout(req)
    return redirect ('login_view')