from django.shortcuts import render, redirect
from stuapp.models import *

def home_view(req):
    data=stuinfo.objects.all()

    context={
        "stu": data
    }
    return render (req,"home.html",context)

def add_stu(req):
    if req.method=="POST":
        name=req.POST.get('name')
        address=req.POST.get('address')
        email=req.POST.get('email')
        age=req.POST.get('age')

        stuinfo.objects.create(
        name=name,
        address=address,
        email=email,
        age=age
        )
        return redirect("home")
    return render(req, "addstu.html")