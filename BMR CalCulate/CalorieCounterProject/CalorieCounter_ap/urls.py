from django.urls import path
from CalorieCounter_ap.views import *

urlpatterns = [
    path('', login_view, name='login_view'),
]