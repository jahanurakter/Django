from django.urls import path
from products.views import *


urlpatterns = [
    path("", home_view, name="home"),
    path("add_products/", add_products, name="add_products"),
    path("product_list/", product_list, name="product_list"),
    path("delete/<str:p_id>", delete_product, name="delete_product"),
    
]