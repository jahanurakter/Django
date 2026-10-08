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
        'form_data':form_data,
        'form_page':'loginpage',
        'form_title':'Login Your Account',
        'form_btn':'Login',
        
    }
    return render(req, 'master/base-from.html', context)

def register_view(req):
    form_data = RegisterForm()
    if req.method == "POST":
        form_data=RegisterForm(req.POST)
        if form_data.is_valid():
            form_data.save()
            return redirect('login_view')

    context={
        'form_data':form_data,
        'form_page':'registerpage',
        'form_title':'Register Your Account',
        'form_btn':'Register',
    }
    return render (req, 'master/base-from.html',context)

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
        'form_data':form_data,
        'form_page':'add_category',
        'form_title':'Category Information',
        'form_btn':'Add Category',
    }

    return render(req, 'master/base-from.html',context)

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
        'form_data':form_data,
        'form_page':'update_category',
        'form_title':' Update Category Information',
        'form_btn':'Update Category',
    }

    return render(req, 'master/base-from.html',context)

def category_delete(req, id):
    # CategoryModel.objects.get(id=id).delete()
    get_object_or_404(CategoryModel, id=id).delete()

    return redirect('category_list')

def add_product(req):
    form_data=ProductForm()
    if req.method == "POST":
        form_data=ProductForm(req.POST)
        if form_data.is_valid():
            data=form_data.save(commit=False)
            data.total_amount=data.price*data.qty
            data.created_by=req.user
            data.save()
            return redirect('product_list')
    context={
        "form_data":form_data,
        'form_page':'update_category',
        'form_title':'Add Product Information',
        'form_btn':'Add Product',
        }
    return render(req, 'master/base-from.html',context)

def product_list(req): 
    product_data=ProductModel.objects.filter(created_by = req.user)
    context={
        'product_data':product_data
    }
    return render(req, 'product_list.html',context)

def product_update(req, id):

    product_data=get_object_or_404(ProductModel, id=id)
    form_data=ProductForm(instance=product_data)

    if req.method == "POST":
        form_data=ProductForm(req.POST, instance=product_data)
        if form_data.is_valid():
            data=form_data.save(commit=False)
            data.total_amount=data.price*data.qty
            data.created_by=req.user
            data.save()
            return redirect('product_list')
    context={
            'form_data':form_data,
            'form_page':'update_product',
            'form_title':' Update Product Information',
            'form_btn':'Update Product',
        }
    return render(req, 'master/base-from.html', context)

def product_delete(req, id):
    get_object_or_404(ProductModel, id=id).delete()

    return redirect('product_list')
