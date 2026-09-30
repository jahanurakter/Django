from django.urls import path
from project.views import *

urlpatterns = [
    path('',login_view, name='login_view'),
    path('register/', register_view, name='register_view'),
    path('dashboard/', dashboard_view, name='dashboard_view'),
    path('login/', login_view, name='login_view'),
    path('logout/', logout_view, name='logout_view'),

    path('add_project/', add_project, name='add_project'),
    path('project_list/', project_list, name='project_list'),
    path('update/<str:id>', update, name='update_project'),
    path('delete/<str:id>', delete, name='delete_project')


]