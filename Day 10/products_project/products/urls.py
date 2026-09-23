from django.urls import path
from products.views import *

urlpatterns = [
    path('', home_view, name="home"),
    path('add/', add_products, name="add_products" ),
    path("list/", product_list, name="product_list"),
    path('filter/', product_filter, name="product_filter")
    
]

