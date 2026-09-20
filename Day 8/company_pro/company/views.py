from django.shortcuts import render, redirect
from company.models import *

def home_view(req):

    return render(req, 'home.html')

def employe(req):        
    e_data = employee.objects.all()

    context={
        'e_data': e_data,
    }

    if req.method=='POST':
        e_name= req.POST.get('name')
        e_email=req.POST.get('email')
        e_position=req.POST.get('position')

        employee.objects.create(
            name=e_name,
            email=e_email,
            position=e_position

        )
        return redirect(employe)

    return render(req, 'employee.html', context)
