from django.shortcuts import render
from userapp.models import *

def home_view(req):
    title= student.objects.all()
    context= {
        "title":title
    }
    return render (req, "home.html", context)

def reg_view(req):
    data_set= info.objects.all()
    context={
        "data_set": data_set,
    }
    return render (req,"reg.html",context)
