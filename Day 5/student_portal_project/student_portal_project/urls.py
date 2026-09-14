
from django.contrib import admin
from django.urls import path
from students.views import *



urlpatterns = [
    path('admin/', admin.site.urls),
    path("home/",home_view,name="Home"),
    path("", home_view, name="Home" ),
    path("about/", about_view, name= "About"),
    path("s_list/", list_view, name="Student_List"),
    path("s_details/", details_view, name="Student_Details")
  
]
