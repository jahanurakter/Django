from django.urls import path
from api_app.views import *

urlpatterns = [
    path('product_details/<str:id>/', product_details, name='product_details'),
    path('products/', product_view, name='product_view')
]