from django.urls import path
from form_app.views import *

urlpatterns = [
    path('',login_view,name='login_view'),
    path('home/',home_view,name='home_view'),
    
    path('register/', register_view, name= 'register_view'),
    path('logout/', logout_view, name= 'logout_view'),
    path('category_add/', category_add, name= 'category_add'),
    path('category_list/', category_list, name= 'category_list'),
    path('category_update/<str:id>/', category_update, name= 'category_update'),
    path('category_delete/<str:id>/', category_delete, name= 'category_delete'),
    
    
]