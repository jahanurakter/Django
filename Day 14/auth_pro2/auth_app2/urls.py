from django.urls import path
from auth_app2.views import *

urlpatterns = [
    path('',login_view, name="login_view"),
    path('register/', register_view, name='register_view'),
    path('dashboard/', dashboard_view, name='dashboard_view'),
    path('logout/', logout_view, name='logout_view'),
]