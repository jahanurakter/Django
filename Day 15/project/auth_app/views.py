from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from auth_app.models import *

def register_view(req):
    if req.method == 'POST':
        username=req.POST.get('username')
        email=req.POST.get('email')
        image=req.FILES.get('image')
        user_type=req.POST.get('user_type')
        password=req.POST.get('password')
        conf_password=req.POST.get('conf_password')

        user_exist=AbstractModel.objects.filter(username=username).exists()

        if user_exist:
            print("User Already exist")
            return redirect('register_view')

        if password == conf_password:
            AbstractModel.objects.create_user(
                username=username,
                email=email,
                image=image,
                user_type=user_type,
                password=password
            )
            return redirect('login_view')
    return render(req, 'register.html')

def login_view(req):
    if req.method == 'POST':
        username=req.POST.get('username')
        password=req.POST.get('password')
        user=authenticate(req, username=username, password=password)

        if user:
            login(req,user)
            return redirect('dashboard_view')
        else:
            print('Invalid Password')
    return render(req, 'login.html')

@login_required
def dashboard_view(req):

    return render(req, 'dashboard.html')

def logout_view(req):
    logout(req)
    return redirect('login_view')

def product_add(req):
    if req.method == 'POST':
        name=req.POST.get('name')
        phone=req.POST.get('phone')
        price=req.POST.get('price')

        ProductModel.objects.create(
            name=name,
            phone=phone,
            price=price,
            created_by=req.user
        )

        return redirect('product_list')

    return render(req, 'product_add.html')

def product_list(req):

    data=ProductModel.objects.filter(created_by = req.user)
    context={
        "data":data
    }
    return render(req, 'product_list.html', context)
        


