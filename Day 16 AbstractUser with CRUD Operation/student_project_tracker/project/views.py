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
        student_name=req.POST.get('student_name')
        student_id=req.POST.get('student_id')
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
                student_name=student_name,
                student_id=student_id,
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

def add_project(req):
    if req.method == 'POST':
        project_name=req.POST.get('project_name')
        project_description=req.POST.get('project_description')
        project_image=req.FILES.get('project_image')
        project_status=req.POST.get('project_status')

        ProjectModel.objects.create(
            project_name=project_name,
            project_description=project_description,
            project_image=project_image,
            project_status=project_status,
            created_by=req.user
        )
        return redirect('project_list')
    return render (req, 'add_project.html')

def project_list(req):
    project_data=ProjectModel.objects.filter(created_by = req.user)         #jar jar project se se dekhte pabe ti filter use kora

    context={
        'project_data':project_data
    }
    return render(req, 'project_list.html', context)


def update(req, id):
    data=ProjectModel.objects.get(id=id)

    if req.method == "POST":

        project_name=req.POST.get('project_name')
        project_status=req.POST.get('project_status')
        project_description=req.POST.get('project_description')
        project_image=req.FILES.get('project_image')

        data.project_name=project_name
        data.project_status=project_status
        data.project_description=project_description
        if project_image:
            data.project_image=project_image

        data.save()
        return redirect('project_list')
    context={
        "project_data":data
    }
    return render(req, 'update.html',context)

def delete(req, id):
    ProjectModel.objects.get(id=id).delete()

    return redirect('project_list')