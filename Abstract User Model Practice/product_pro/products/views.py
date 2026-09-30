from django.shortcuts import render,redirect
from products.models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

def login_view(req):

    return render(req, 'login.html')

def register_view(req):

    return render (req, 'register.html')

def dashboard_view(req):

    return render(req, 'dashboard.html')


def logout_view(req):
    logout(req)
    return redirect('login_view')



