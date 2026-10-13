from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from CalorieCounter_ap.models import *
from CalorieCounter_ap.forms import *
from django.contrib.auth.forms import AuthenticationForm
from django.db.models import Sum

def login_view(req):
    form_data=AuthenticationForm()
    if req.method == 'POST':
        form_data=AuthenticationForm(req, data=req.POST)
        if form_data.is_valid():
            user=form_data.get_user()
            if user:
                login(req, user)
            return redirect('dashboard_view')
    context={
            "form_data": form_data,
            "form_page":'login',
            "form_title":'Login Your Account',
            "form_btn":'Login',
            'extra_link': 'register',
            'extra_text': "Don't have any account?",
            }
    return render(req, 'master/form-base.html',context)

def register_view(req):
    form_data=RegistrationForm()
    if req.method == 'POST':
        form_data=RegistrationForm(req.POST)
        if form_data.is_valid():
            form_data.save()
            return redirect('login_view')

    context={
            "form_data": form_data,
            "form_page":'regsiter',
            "form_title":'Registration Form',
            "form_btn":'Register',
            'extra_link': 'login',
            'extra_text': 'Already have an account?',
        }
    return render(req, 'master/form-base.html',context)


def dashboard_view(req):
    try:
        bmr=req.user.user_profile.bmr
    except:
        bmr=0
        messages.warning(req, 'Please Update Your Profile First')
        return redirect('profile_update')
    
    data=ConsumedCalorieModel.objects.filter(user=req.user).aggregate(
        total_calorie=Sum('consumed_calorie')
    )
    total_consumed_calorie=data['total_calorie'] or 0
    less_Or_more = bmr - total_consumed_calorie
    if total_consumed_calorie > bmr:
        suggestion = "You will be fat"
    else:
        suggestion = "You are fit"
    context={
        'bmr': round(bmr, 2),
        'total_consumed_calorie': round(total_consumed_calorie,2),
        'less_Or_more':round(less_Or_more,2),
        'suggestion': suggestion
    }
    return render (req, 'dashboard.html',context)

def logout_view(req):
    logout(req)
    return redirect('login_view')

def profile_page(req):
    try:
        bmr=req.user.user_profile.bmr
    except:
        bmr=0
        messages.warning(req, 'Please Update Your Profile First')
        return redirect('profile_update')
    return render(req, 'profile.html')

def profile_update(req):

    current_user=req.user
    try:
        profile_data=current_user.user_profile
        print('profile_data')
    except:
        profile_data=None
    
    form_data=UpdateProfileForm(instance=profile_data)
    if req.method == 'POST':
        form_data=UpdateProfileForm(req.POST, req.FILES, instance=profile_data)
        if form_data.is_valid():
            form_data=form_data.save(commit=False)
            form_data.user=current_user
            if form_data == 'Male':
                #BMR= 66.47+(13.75 x weight in kg) + (5.003 x height in cm) - (6.755 x age in years) 
                form_data.bmr = 66.47+(13.75*form_data.weight) + (5.003*form_data.height) - (6.755*form_data.age)
                #BMR=655.1+(9.563*form_data.weight)+(1.850*form_data.height) - (4.676*form_data.age)
            else:
                form_data.bmr = 655.1+(9.563*form_data.weight) + (1.850*form_data.height) - (4.676*form_data.age)
                form_data.save()
            return redirect('profile_page')

    context={
            "form_data": form_data,
            "form_page":'profile_update',
            "form_title":'Profile Update Form',
            "form_btn":'Update',
    
        }    
    return render(req, 'master/form-base.html',context)

def calorie_consumed_list(req):
    try:
        bmr=req.user.user_profile.bmr
    except:
        bmr=0
        messages.warning(req, 'Please Update Your Profile First')
        return redirect('profile_update')
    consumed_calorie=ConsumedCalorieModel.objects.filter(user = req.user)
    context={
        'consumed_calorie':consumed_calorie
    }

    return render(req, 'calorie_list.html',context)

def add_consumed_calorie(req):

    form_data=ConsumeCalorieForm()
    if req.method == 'POST':
        form_data=ConsumeCalorieForm(req.POST)
        if form_data.is_valid():
            form_data=form_data.save(commit=False)
            form_data.user=req.user
            form_data.save()
            return redirect('calorie_list')

    context={
            "form_data": form_data,
            "form_page":'add_consumed_calorie',
            "form_title":'Calorie Consumed Form',
            "form_btn":'Add Calorie',
            
        }
    
    return render(req, 'master/form-base.html',context)

def update_consumed_calorie(req,id):
    data=get_object_or_404(ConsumedCalorieModel, id=id)
    form_data=ConsumeCalorieForm(instance=data)
    if req.method == 'POST':
        form_data=ConsumeCalorieForm(req.POST, instance=data)
        if form_data.is_valid():
            form_data=form_data.save(commit=False)
            form_data.user=req.user
            form_data.save()
            return redirect('calorie_list')

    context={
            "form_data": form_data,
            "form_page":'update_consumed_calorie',
            "form_title":'Update Calorie Consumed Form',
            "form_btn":'Update Calorie',
            
        }
    
    return render(req, 'master/form-base.html',context)

def delete_carlorie(req,id):
    get_object_or_404(ConsumedCalorieModel, id=id).delete()

    return redirect('calorie_list')