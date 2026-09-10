from django.http import HttpResponse

def false(req):
    return HttpResponse("False app")
