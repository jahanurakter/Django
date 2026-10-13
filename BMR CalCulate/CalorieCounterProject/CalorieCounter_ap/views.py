from django.shortcuts import render,redirect,get_object_or_404
from CalorieCounter_ap.models import *
from CalorieCounter_ap.forms import *


def login_view(req):
    return render(req, 'login.html')