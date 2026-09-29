from django.urls import path
from auth_app.views import *

urlpatterns = [
    path('register/', register_view, name='register_view'),
    path('', login_view, name='login_view'),
    path('dashboard/', dashboard_view, name='dashboard_view'),
    path('logout/', logout_view, name='logout_view'),
    path('product_add/', product_add, name='product_add'),
    path('product_list/', product_list, name='product_list'),

]