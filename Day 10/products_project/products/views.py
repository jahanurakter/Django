from django.shortcuts import render, redirect
from products.models import *

def home_view(req):

    return render(req, "home.html")


def product_list(req):
    data=ProductModel.objects.all()

    context={
        "p_id": data
    }
    return render(req, "product_list.html",context)


def add_products(req):
    if req.method == "POST":
        name=req.POST.get("name")
        description=req.POST.get("description")
        price=req.POST.get("price")
        date=req.POST.get("date")
        image=req.FILE.get("image")
        ProductModel.objects.create(
            name=name,
            description=description,
            price=price,
            date=date,
            image=image
        )
        return redirect("product_list")         #url name parameter
    return render(req, "add_products.html")


def product_filter(req):

    return render(req, "product_filter.html")