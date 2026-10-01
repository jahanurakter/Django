from django.shortcuts import render,redirect
from django.contrib import messages ##########
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from project.models import *

def login_view(req):
    if req.method == "POST":
        username=req.POST.get('username')
        password=req.POST.get('password')
        user=authenticate(req, username=username, password=password)
        if user:
            login(req, user)
            return redirect('dashboard_view')
        else:
            messages.warning(req, "Invalid Credentials")
        
    return render(req,'login.html')

def register_view(req):
    if req.method == "POST":
        username=req.POST.get('username')
        email=req.POST.get('email')
        user_type=req.POST.get('user_type')
        password=req.POST.get('password')
        conf_password=req.POST.get('conf_password')

        user_exist=UserModel.objects.filter(username=username).exists()
        if user_exist:
            messages.warning(req, "User Already Exist") ##########
            return redirect('register_view')
        if password == conf_password:
            UserModel.objects.create_user(
                username=username,
                email=email,
                user_type=user_type,
                password=password
            )
            return redirect('login_view')

    return render(req, 'register.html')

@login_required
def dashboard_view(req):

    return render(req,'dashboard.html')

def logout_view(req):
    logout(req)
    
    return redirect('login_view')

def update_view(req):

    return render(req, 'update.html')


