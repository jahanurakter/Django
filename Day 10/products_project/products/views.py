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
        product_type=req.POST.get("product_type")
        description=req.POST.get("description")
        price=req.POST.get("price")
        date=req.POST.get("date")
        image=req.FILES.get("image")

        ProductModel.objects.create(
            name = name,
            product_type=product_type,
            description = description,
            price = price,
            product_date = date,
            image = image,
        )
        return redirect("product_list")         #url name parameter
    
    return render(req, "add_products.html")


def product_filter(req):

    return render(req, "product_filter.html")

def delete_product(req, p_id):

    ProductModel.objects.get(id = p_id).delete()

    return redirect("product_list")

def update_product(req, p_id):

    p_data=ProductModel.objects.get(id = p_id)

    if req.method == "POST":
        name=req.POST.get("name")
        product_type=req.POST.get("product_type")
        description=req.POST.get("description")
        price=req.POST.get("price")
        date=req.POST.get("date")
        image=req.FILES.get("image")

        p_data.name=name
        p_data.product_type=product_type
        p_data.description=description
        p_data.price=price
        p_data.date=date
        if image:
            p_data.image=image

        p_data.save()
        return redirect("product_list")
    context={
        "p_data":p_data
    }

    return render(req, "update_product.html", context)
    