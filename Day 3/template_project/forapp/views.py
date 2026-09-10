from django.shortcuts import render

def home_view(req):

    return render(req, "our.html")

def my_view(req):
    return render (req, "about.html")

def service_view(req):
    return render (req, "service.html")

def contact_view(req):
    return render (req, "contact.html")
