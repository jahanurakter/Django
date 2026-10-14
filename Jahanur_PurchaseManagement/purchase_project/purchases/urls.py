from django.urls import path
from purchases.views import *

urlpatterns = [
    path('',login_view, name='login_view'),
    path('register/',register_view, name='register_view'),
    path('dashboard/',dashboard_view, name='dashboard_view'),
    path('logout/',logout_view, name='logout_view'),

    path('profile/', profile_page, name='profile_page'),
    path('update_profile/', update_profile, name='update_profile'),

    path('add_supplier/', add_supplier, name='add_supplier'),
    path('supplier_list/', supplier_list, name='supplier_list'),
    path('update_supplier/<str:id>/', supplier_update, name='update_supplier'),
    path('delete_supplier/<str:id>/', delete_supplier, name='delete_supplier'),


]