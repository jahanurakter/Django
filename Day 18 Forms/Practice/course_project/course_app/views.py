from django.shortcuts import render,redirect,get_object_or_404
from course_app.models import *
from course_app.forms import *

def home_view(req):
    return render(req, 'home.html')

def add_course(req):
    course_data = CourseForm()
    if req.method == "POST":
        course_data=CourseForm(req.POST, req.FILES)
        if course_data.is_valid():
            course_data.save()
            return redirect("course_list")
    context={
        'course_data':course_data
    }
    return render(req, 'add_course.html', context)


def course_list(req):
    course_data = CourseModel.objects.all()
    context={
        'course_data':course_data
    }
    return render(req, 'course_list.html',context)

def update_course(req, id):
    form_course=get_object_or_404(CourseModel, id=id)
    course_data = CourseForm(instance=form_course)
    if req.method == "POST":
        course_data=CourseForm(req.POST, req.FILES, instance=form_course)
        if course_data.is_valid():
            course_data.save()
            return redirect("course_list")
    context={
        'course_data':course_data
    }
    return render(req, 'update_course.html', context)