from django.urls import path
from company.views import *

urlpatterns = [
    path("", home_view, name="home"),
    path('employee/',employe, name="employee"),
]
