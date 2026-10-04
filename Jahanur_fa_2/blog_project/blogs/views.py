from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from blogs.models import*

def login_view(req):
    if req.method == 'POST':
        username=req.POST.get('username')
        password=req.POST.get('password')

        user = authenticate(req, username=username, password=password)
        if user:
            login(req, user)
            return redirect('home_view')
        else:
            messages.warning(req, "Invalid Credentials")
        
    return render(req,'login.html')


def register_view(req):
    if req.method == 'POST':
        username=req.POST.get('username')
        full_name=req.POST.get('full_name')
        email=req.POST.get('email')
        password=req.POST.get('password')
        conf_password=req.POST.get('conf_password')

        user_exist=UserModel.objects.filter(username=username).exists()
        if user_exist:
            messages.warning(req, "User Already Exist....")
            return redirect("register_view")
        else:
            messages.success(req, "Register Succesfully")

        if password == conf_password:
                UserModel.objects.create_user(
                username=username,
                full_name=full_name,
                email=email,
                password=password,
                )
                return redirect('login_view')

    return render(req, 'register.html')

@login_required
def home_view(req):
    return render(req, 'home.html')

def logout_view(req):
    logout(req)
    return redirect('login_view')

def blog_list_view(req):
    
    data=BlogModel.objects.all()
    context = {
        "blog_data":data
        }
    return render(req,"blog_list.html", context)

def blogpost_view(req):
    if req.method == "POST":
        title=req.POST.get('title')
        author_name=req.POST.get('author_name')
        content=req.POST.get('content')
        category=req.POST.get('category')
        blog_image=req.FILES.get('blog_image')


        BlogModel.objects.create(
            title=title,
            author_name=author_name,
            content=content,
            category=category,
            blog_image=blog_image,
           
        )
        return redirect('blog_list')
        
    return render(req,"blogpost.html")

def upadate_view(req, id):
    data=BlogModel.objects.get(id = id)
    if req.method == "POST":
        title=req.POST.get('title')
        author_name=req.POST.get('author_name')
        content=req.POST.get('content')
        category=req.POST.get('category')
        blog_image=req.FILES.get('blog_image')

        data.title=title
        data.author_name=author_name
        data.content=content
        data.category=category
        if blog_image:
            data.blog_image=blog_image

        data.save()
        return redirect('blog_list')

    context={
        "blog_data":data
    }

    return render(req,'update.html',context)

def delete_view(req, id):
    BlogModel.objects.get(id=id).delete()
    logout(req)

    return redirect('blog_list')