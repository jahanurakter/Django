from django.urls import path
from CalorieCounter_ap.views import *

urlpatterns = [
    path('', login_view, name='login_view'),
    path('register/', register_view, name='register_view'),
    path('dashboard/', dashboard_view, name='dashboard_view'),
    path('logout/', logout_view, name='logout_view'),

    path('profile/',profile_page, name='profile_page'),
    path('profile_update/',profile_update, name='profile_update'),
    path('calorie_list/',calorie_consumed_list, name='calorie_list'),
    path('add_consumed_calorie/',add_consumed_calorie, name='add_consumed_calorie'),
    path('update_consumed_calorie/<str:id>/',update_consumed_calorie, name='update_consumed_calorie'),
    path('delete_carlorie/<str:id>/',delete_carlorie, name='delete_carlorie'),
]