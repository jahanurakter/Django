from django.shortcuts import render
def home_view(req):
    context={
        "title":"Student Information"
    }
    return render(req, "home.html", context)

def about_view(req):
    context={
        "about": "About Student"
    }
    return render(req, "about.html", context)

def list_view(req):
    context = {
        "list":"Student List",
        "stu":{
        "info":{
            "id":101,
            "name": "Jeffy",
            "dept": "CSE",
            "batch": 232,
            "gpa": 4.67
        }
        }
    }
    return render(req, "list.html", context)

def details_view(req):
    context = {
        "details":"Student Details",
    }
    return render(req, "details.html", context)

