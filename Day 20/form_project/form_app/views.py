from django.shortcuts import render,redirect,get_object_or_404
from form_app.forms import *
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
@login_required
def home_view(req):

    return render(req, 'home.html')

def login_view(req):
    form_data=AuthenticationForm()
    if req.method == "POST":
        form_data=AuthenticationForm(req, data=req.POST)
        if form_data.is_valid():
            
            user=form_data.get_user()
            if user:
                login(req,user)
                return redirect('home_view')
    context={
        'form_data':form_data
    }
    return render(req, 'login.html', context)

def register_view(req):
    form_data = RegisterForm()
    if req.method == "POST":
        form_data=RegisterForm(req.POST)
        if form_data.is_valid():
            form_data.save()
            return redirect('login_view')

    context={
        'form_data':form_data
    }
    return render (req, 'register.html',context)

def logout_view(req):
    logout(req)
    return redirect('login_view')

def category_add(req):
    form_data=CategoryForm()
    if req.method == "POST":
        form_data=CategoryForm(req.POST)
        if form_data.is_valid():
            form_data.save()
            return redirect('category_list')
    context={
        "form_data":form_data
    }

    return render(req, 'category_add.html',context)

def category_list(req):
    category_data=CategoryModel.objects.all()
    context={
        'category_data':category_data
    }
    return render(req, 'category_list.html', context)

def category_update(req,id):
    category_data=get_object_or_404(CategoryModel, id=id)
    form_data=CategoryForm(instance=category_data)
    if req.method == "POST":
        form_data=CategoryForm(req.POST, instance=category_data)
        if form_data.is_valid():
            form_data.save()
            return redirect('category_list')
    context={
        "form_data":form_data
    }

    return render(req, 'category_update.html',context)

def category_delete(req, id):

    # CategoryModel.objects.get(id=id).delete()
    get_object_or_404(CategoryModel, id=id).delete()

    return redirect('category_list')