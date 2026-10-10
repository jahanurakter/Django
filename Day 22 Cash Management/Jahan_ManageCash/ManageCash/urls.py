from django.urls import path
from ManageCash.views import *


urlpatterns = [
    path('', login_view, name='login_view'),
    path('dashboard/',dashboard_view, name ='dashboard_view'),
    path('register/', register_view, name = 'register_view'),
    path('logout/', logout_view, name='logout_view'),

    path('addcash_list/', addcash_list, name='addcash_list'),    
    path('addcash_view/', addcash_view, name='addcash_view'),    
    path('cash_update/<str:id>/', cash_update, name='cash_update'),    
    path('cash_delete/<str:id>/', cash_delete, name='cash_delete'),  


    path('expense_view/', expense_view, name='expense_view'),
    path('expense_list/', expense_list, name='expense_list'),
    path('update_expense/<str:id>/', update_expense, name='update_expense'),
    path('delete_expense/<str:id>/', delete_expense, name='delete_expense'),
     
]