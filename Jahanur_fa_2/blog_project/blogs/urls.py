from django.urls import path
from blogs.views import *

urlpatterns = [
    path('',login_view, name='login_view'),
    path('register/', register_view, name='register_view'),
    path('logout/', logout_view, name='logout_view'),
    
    path('home/', home_view, name='home_view'),
    path('post/', blogpost_view, name='blog_post'),
    path('blog_list', blog_list_view, name='blog_list'),
    path('update/<str:id>/', upadate_view, name="update_view"),
    path('delete/<str:id>/',delete_view, name="delete_view")
]