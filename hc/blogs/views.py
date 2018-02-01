import requests
from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.contrib import messages
from django.urls import reverse
from hc.lib import emails
from hc.blogs.models import Blog, Category
from django.contrib.auth.models import User
from hc.blogs.forms import (CreateBlogForm, CreateCategoryForm, ShareBlogForm)

def blog(request):
    if request.method == "POST":      
        if "add_category" in request.POST: 
            form = CreateCategoryForm(request.POST) 
            if form.is_valid():
                name = form.cleaned_data["name"]
                for key, value in dict(request.POST).items():
                    if key == 'name':
                        category = Category() 
                        category.name = ', '.join(value)
                        category.save()
                        
            return redirect("hc-blog")
    #Query from the category table to get category name    

    categories = Category.objects.all()
    ctx = {"page": "blog", "categories":categories}
    return render(request, "blogs/blog.html", ctx)

@login_required
def add_blog(request, cat_id):
    if request.method == "POST":
        form = CreateBlogForm(request.POST)
        if form.is_valid():
            title = request.POST['title']
            blog = form.cleaned_data['body']
            category = Category.objects.get(id=cat_id)
            author = request.user
            created_date = timezone.now()
            blog = Blog(title=title, body=blog,category=category,created_date=created_date, author=author)
            blog.save()

            return redirect("hc-add-blog", cat_id=cat_id)
    else:
        form = CreateBlogForm()

    ctx = {"page": "blog", "form": form, "id": cat_id}
    return render(request, "blogs/add_blog.html", ctx)

def send_blog_link(self, cat_id, blog_id, inviting_profile=None):
    user = Profile.objects.all()
    path = reverse("hc-single-blog", kwargs={'cat_id':cat_id, 'blog_id':blog_id})
    ctx = {
        "blog_link": settings.SITE_ROOT + path,
        "inviting_profile": inviting_profile,
    }
    emails.share_blog(self, ctx, cat_id, blog_id)

def view_blog(request, cat_id):
    category = Category.objects.get(id=cat_id)
    q = Blog.objects.filter(category=category).order_by('created_date')
    blogs = list(q)

    return render(request, "blogs/view_blog.html", {"blogs": blogs , "category":category.id})

def view_single_blog(request, cat_id, blog_id):
    category = Category.objects.get(id=cat_id)
    blog = Blog.objects.get(id=blog_id, category=category)
    if request.method == "POST":
        if "share-blog" in request.POST:
            form = ShareBlogForm(request.POST)
            if form.is_valid():
                # send an email
                email = form.cleaned_data["email"]

            send_blog_link(email, cat_id, blog_id)
            messages.success(request, "Blog link shared to %s" % email)

    return render(request, "blogs/single_blog.html", {"blog":blog, "category":category.id , "id":blog_id})

def delete_blog(request, blog_id, cat_id):
    # delete blog
    blog = Blog.objects.get(id=blog_id)
    blog.delete()
    messages.info(request, "Blog deleted!")
    return redirect("hc-view-blog", cat_id=cat_id)

def delete_category(request, cat_id):
    # delete category
    category = Category.objects.get(id=cat_id)
    category.delete()
    messages.info(request, "Category deleted!")
    return redirect("hc-blog")
