from django.urls import path
from stuapp.views import *

urlpatterns = [
    path("", home_view, name="home"),
    path("student_add/", add_stu, name="addstudent"),
]