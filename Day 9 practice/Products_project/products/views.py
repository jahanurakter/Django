from django.shortcuts import render, redirect
from products.models import *

def home_view(req):

    return render(req, 'home.html')

def product_list(req):
    data=ProductModel.objects.all()
    context={
        "product":data
    }
    return render(req, "product_list.html",context)

def add_products(req):

    if req.method == "POST":

        name = req.POST.get("name")
        description = req.POST.get("description")
        price = req.POST.get("price")
        p_date = req.POST.get("date")
        image = req.FILES.get("image")

        ProductModel.objects.create(

            name = name,
            description = description,
            price = price,
            product_date = p_date,
            image = image,
        )

        return redirect("product_list")

    return render(req, "add_products.html")

def delete_product(req, p_id):

    ProductModel.objects.get(id = p_id).delete()

    return render(req, "delete.html")
