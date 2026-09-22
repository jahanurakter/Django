from django.shortcuts import render,redirect
from products.models import *

def home_view(req):
    
    return render (req, 'home.html')

def products_list(req):
        list = ProductModel.objects.all()
        filter_list= ProductModel.objects.filter(price__gt = 100)
        mouse_list = ProductModel.objects.filter(name = "Mouse")    
        context={
               "products_list": list,
               "filter_list": filter_list,
               "mouse_list": mouse_list
            
        }

        return render(req, "products_list.html" , context)

def add_product(req):
        
    if req.method == "POST":
        name = req.POST.get('name')
        description = req.POST.get("description")
        date = req.POST.get("date")
        price = req.POST.get("price")
        image = req.FILES.get("image")

        ProductModel.objects.create(
            name = name,
            description = description,
            price = price,
            production_date = date,
            image = image
            )

        return redirect("products_list")

    return render(req, "add_product.html")

def delete_view(req, p_id):
     
     ProductModel.objects.get(id = p_id).delete()

     return redirect("products_list")

def update_view(req, p_id):
    pro_data= ProductModel.objects.get(id = p_id)
    if req.method == "POST":
        name = req.POST.get('name')
        description = req.POST.get("description")
        date = req.POST.get("date")
        price = req.POST.get("price")
        image = req.FILES.get("image")

        pro_data.name = name
        pro_data.description = description
        pro_data.date = date
        pro_data.price = price
        if image:
            pro_data.image = image

        pro_data.save()

        return redirect("products_list")
    
    context = {
         "pro_data":pro_data
    }
    return render(req, "update_product.html",context)


    

