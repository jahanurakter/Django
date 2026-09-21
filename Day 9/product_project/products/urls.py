from django.urls import path
from products.views import *

urlpatterns = [
    path("", home_view, name="home"),
    path("add_products/", add_product, name="add_products"),
    path("list/", products_list, name="products_list")
]