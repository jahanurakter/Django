from django.shortcuts import render,redirect
from education.models import *

def home_view(req):

    return render(req, "home.html")

def student_list(req):
    data=StudentModel.objects.all()

    context={
        "stu_data":data
    }
    return render(req, "stu_list.html",context)

def student_add(req):

    if req.method == "POST":
        name=req.POST.get("name")
        image=req.FILES.get("image")
        date=req.POST.get("date")
        course_name=req.POST.get("course_name")
        course_fee=req.POST.get("course_fee")

        StudentModel.objects.create(
            stu_name=name,
            stu_image=image,
            admission_date=date,
            course_name=course_name,
            course_fee=course_fee,
        )
        return redirect("student_list")
        
    return render(req, "student_add.html")

def student_delete_view(req, p_id):

    StudentModel.objects.get(id = p_id).delete()

    return redirect("student_list")

def student_update(req, id):

    data=StudentModel.objects.get(id = id)

    if req.method == "POST":
            name=req.POST.get("name")
            image=req.FILES.get("image")
            date=req.POST.get("date")
            course_name=req.POST.get("course_name")
            course_fee=req.POST.get("course_fee")

            data.name=name
            if image:
                 data.image=image
            data.date=date
            data.course_name=course_name
            data.course_fee=course_fee

            data.save()
            return redirect ("student_list")

    context={
         "data":data
    }

    return render(req, "update.html",context)    

def result_list(req):

    result_data=ResultModel.objects.all()
    context={
         "result_data":result_data
    }

    return render(req, "result_list.html",context)

def add_result(req):
        if req.method == "POST":
                name=req.POST.get("name")
                marks=req.POST.get("marks")
                grade=req.POST.get("grade")
        
                ResultModel.objects.create(
                    stu_name=name,
                    marks=marks,
                    grade=grade
                )
                return redirect("result_list")
          
     
        return render(req, "add_result.html")

def delete_result(req, id):

    ResultModel.objects.get(id=id).delete()

    return redirect("result_list")

def update_result(req, id):

    data = ResultModel.objects.get(id=id)
      
    if req.method == "POST":
        name=req.POST.get("name")
        marks=req.POST.get("marks")
        grade=req.POST.get("grade")
             
         
        data.stu_name=name
        data.marks=marks
        data.grade=grade

        data.save()

        return redirect("result_list")
      
    context={
         
           "data":data
      }         
          
    return render(req, "update_result.html", context)

     
     
