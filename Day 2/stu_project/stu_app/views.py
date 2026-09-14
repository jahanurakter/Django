from django.http import HttpResponse

def home_view(req):

    return HttpResponse("Welcome Home")

def about_home(req):

    return HttpResponse("About Home")

def contact(req):
    return HttpResponse("Contact Home")

def student(req):
    return HttpResponse("Student List")
def teacher(req):
    return HttpResponse("Teacher List")
def course(req):
    return HttpResponse("Course List")
def dept(req):
    return HttpResponse("Dept List")

