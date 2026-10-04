from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from blogs.models import*

def login_view(req):
    if req.method == 'POST':
        username=req.POST.get('username')
        password=req.POST.get('password')

        user = authenticate(req, username=username, password=password)
        if user:
            login(req, user)
            return redirect('home_view')
        else:
            messages.warning(req, "Invalid Credentials")
        
    return render(req,'login.html')


def register_view(req):
    if req.method == 'POST':
        username=req.POST.get('username')
        full_name=req.POST.get('full_name')
        email=req.POST.get('email')
        password=req.POST.get('password')
        conf_password=req.POST.get('conf_password')

        user_exist=UserModel.objects.filter(username=username).exists()
        if user_exist:
            messages.warning(req, "User Already Exist....")
            return redirect("register_view")
        else:
            messages.success(req, "Register Succesfully")

        if password == conf_password:
                UserModel.objects.create_user(
                username=username,
                full_name=full_name,
                email=email,
                password=password,
                )
                return redirect('login_view')

    return render(req, 'register.html')

def home_view(req):
    return render(req, 'home.html')

def logout_view(req):
    logout(req)
    return redirect('login_view')

