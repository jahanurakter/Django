from django.urls import path
from form_app.views import *

urlpatterns = [
    path('', welcome_view, name='welcome_view'),
    path('add_blog/', add_blog, name='add_blog'),
    path('blog_list/', blog_list, name='blog_list'),
    path('update_blog/<str:id>/', update_blog, name='update_blog'),
]