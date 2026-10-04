from django.urls import path
from blogs.views import *

urlpatterns = [
    path('',login_view, name='login_view'),
    path('register/', register_view, name='register_view'),
    path('logout/', logout_view, name='logout_view'),

    path('home/', home_view, name='home'),
]