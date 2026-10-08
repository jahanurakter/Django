from django.shortcuts import render,redirect,get_list_or_404
from django.contrib.auth.decorators import login_required
from ManageCash.models import *
from ManageCash.forms import *
from django.contrib.auth import authenticate, login, logout

def dashboard_view(req):
    return render(req, 'dashboard.html')

def login_view(req):
    form_data=
    return render (req, 'master/base-form.html')

def register_view(req):
    return render(req, 'master/base-form.html')

def logout_view(req):
    logout(req)
    return redirect ('login_view')