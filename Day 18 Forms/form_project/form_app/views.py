from django.shortcuts import render,redirect, get_object_or_404
from form_app.models import *
from form_app.forms import *

def welcome_view(req):

    return render (req, 'welcome.html')


def add_blog(req):
    form_data= BlogForm()       # empty form pass
    if req.method == "POST":
        form_data= BlogForm(req.POST , req.FILES)
        if form_data.is_valid():
            form_data.save()
            return redirect("blog_list")
    context={
        'form_data': form_data
    }
    return render (req, 'add_blog.html', context)

def blog_list(req):
    blog_data = BlogModel.objects.all()

    context= {
        'blog_data': blog_data
    }
    return render(req, 'blog_list.html',context)

def update_blog(req, id):
    blog_data = get_object_or_404(BlogModel, id=id)
    form_data=BlogForm(instance=blog_data)

    if req.method == "POST":        #data dhorar jonno
        form_data=BlogForm(req.POST, req.FILES, instance=blog_data) #instance e value pass korar jonno 
        if form_data.is_valid():
            form_data.save()
            return redirect('blog_list')

    context={
        'form_data':form_data
    }
    return render(req, 'update.html', context)