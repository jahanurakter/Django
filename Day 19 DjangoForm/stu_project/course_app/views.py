from django.shortcuts import render,redirect, get_object_or_404
from course_app.forms import *
from course_app.models import *

def home_view(req):
    return render (req, 'home.html')

def course_list(req):
    stu_crs=StuModel.objects.all()
    context={
        'stu_crs': stu_crs
    }
    return render (req, 'course_list.html', context)

def stu_course(req):
    stu_crs=StuForm()
    if req.method == "POST":
        stu_crs=StuForm(req.POST, req.FILES)
        if stu_crs.is_valid():
            stu_crs.save()
            return redirect('course_list')
    context={
        'stu_crs':stu_crs
    }
    
    return render (req, 'stu_course.html', context)

def update_course(req, id):
    data=get_object_or_404 (StuModel, id=id)
    stu_crs=StuForm(instance=data)
    if req.method == "POST":
        stu_crs=StuForm(req.POST, req.FILES, instance=data)
        if stu_crs.is_valid():
            stu_crs.save()
            return redirect('course_list')
    context={
            'stu_crs':stu_crs
        }
        
    return render (req, 'update_course.html', context)
    
    