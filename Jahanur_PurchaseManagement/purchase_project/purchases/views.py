from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages
from purchases.models import *
from purchases.forms import *
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login,logout


def login_view(req):
    form_data=AuthenticationForm()
    if req.method == "POST":
        form_data=AuthenticationForm(req, data=req.POST )
        if form_data.is_valid():
            user=form_data.get_user()
            if user:
                login(req, user)
            return redirect('dashboard_view')
    context={
        'form_data': form_data,
        'form_page':'login',
        'form_title':'Login Your Account',
        'from_btn':'Login'

    }
    return render(req, 'master/base-form.html',context)

def register_view(req):
    form_data=RegistrationForm()
    if req.method == "POST":
        form_data=RegistrationForm(req.POST)
        if form_data.is_valid():
            form_data.save()
            return redirect('login_view')
    context={
        'form_data': form_data,
        'form_page':'register',
        'form_title':'Register Your Information',
        'from_btn':'Register'

    }
    return render(req, 'master/base-form.html',context)

def dashboard_view(req):

    return render(req, 'dashboard.html')

def logout_view(req):
    logout(req)
    return redirect('login_view')


def profile_page(req):
    current_user=req.user
    try:
        profile_data=current_user.user_profile
        print('profile_data')
    except:
        profile_data=None
        messages.warning(req, 'Please Update Your Profile First')
        return redirect('update_profile')
    return render(req, 'profile.html')

def update_profile(req):
    current_user=req.user
    try:
        profile_data=current_user.user_profile
        print('profile_data')
    except:
        profile_data=None

    form_data=UserProfileForm(instance=profile_data)
    if req.method == "POST":
        form_data=UserProfileForm(req.POST, req.FILES, instance=profile_data)
        if form_data.is_valid():
            form_data=form_data.save(commit=False)
            form_data.user=current_user
            form_data.save()
            return redirect('profile_page')
    context={
        'form_data': form_data,
        'form_page':'update_form',
        'form_title':'Update Your Information',
        'from_btn':'Update'

    }
    return render(req, 'master/base-form.html', context)


def add_supplier(req):
    if req.method == "POST":
        supplier_name=req.POST.get('supplier_name')
        contact_number=req.POST.get('contact_number')
        address=req.POST.get('address')      

        SupplierModel.objects.create(
            supplier_name=supplier_name,
            contact_number=contact_number,
            address=address
        )
        return redirect('supplier_list')
    return render(req, 'add_supplier.html')

def supplier_list(req):
    supplier_data = SupplierModel.objects.filter(user=req.user)
    context={
        'supplier_data':supplier_data
    }
    return render(req, 'supplier_list.html',context)

def supplier_update(req, id):
    supplier_data = SupplierModel.objects.get(id=id)
    
    if req.method == "POST":
        supplier_name=req.POST.get('supplier_name')
        contact_number=req.POST.get('contact_number')
        address=req.POST.get('address')

        supplier_data.supplier_name=supplier_name,
        supplier_data.contact_number=contact_number,
        supplier_data.address=address

        return redirect('supplier_list')

    context={
            'supplier_data':supplier_data
        }

    return render(req, 'update_supplier.html',context)

def delete_supplier(req,id):
    SupplierModel.objects.get(id=id).delete()
    return redirect('supplier_list')