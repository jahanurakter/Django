from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from auth_app2.models import *

def register_view(req):
    if req.method == 'POST':
        username=req.POST.get('username')
        image=req.FILES.get('image')
        email=req.POST.get('email')
        user_type=req.POST.get('user_type')
        password=req.POST.get('password')
        conf_password=req.POST.get('conf_password')
        if password == conf_password:
            AbstractModel.objects.create_user(
                username=username,
                image=image,
                email=email,
                user_type=user_type,
                password=password,
            )
            return redirect('login_view')

    return render (req, 'register.html')


def login_view(req):

    if req.method == 'POST':
        u_name=req.POST.get('username')
        password=req.POST.get('password')

        user=authenticate(req, username=u_name, password=password)
        if user:
            login(req,user)
            return redirect('dashboard_view')
        else:
            print("Invalid Authentication")

    return render(req,'login.html')
@login_required
def dashboard_view(req):
    return render(req, 'dashboard.html')

@login_required
def logout_view(req):
    logout(req)

    return redirect('login_view')
