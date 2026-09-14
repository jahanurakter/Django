from django.shortcuts import render

def home_view(req):
    context={
        "title":"Student Information",
    }
    return render(req, "home.html", context)



