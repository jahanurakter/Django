from django.urls import path
from course_app.views import *

urlpatterns = [
    path('', home_view, name='home_view'),
    path('stu_course', stu_course, name= 'stu_course'),
    path('course_list', course_list, name= 'course_list'),
    path('update_course/<str:id>/', update_course, name= 'update_course'),
    
]