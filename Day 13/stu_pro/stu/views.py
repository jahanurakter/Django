from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout

def register_view(req):
    if req.method == 'POST':
        username=req.POST.get('username')
        f_name=req.POST.get('f_name')
        l_name=req.POST.get('l_name')
        email=req.POST.get('email')
        password=req.POST.get('password')
        conf_password=req.POST.get('conf_password')
        if password == conf_password:
            User.objects.create_user(
                username=username,
                first_name=f_name,
                last_name=l_name,
                email=email,
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

def dashboard_view(req):
    return render(req, 'dashboard.html')

def logout_view(req):
    logout(req)

    return redirect('login_view')



