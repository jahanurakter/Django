from django.urls import path
from course_app.views import *

urlpatterns = [
    path('', home_view, name='home_view'),
    path('add_course/', add_course, name='add_course'),
    path('course_list/', course_list, name='course_list'),
    path('update_course/<str:id>', update_course, name='update_course'),
    path('delete_view/<str:id>', delete_view, name='delete_view'),
]