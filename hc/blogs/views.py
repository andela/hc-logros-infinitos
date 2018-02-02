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

def categories(request, cat_id=None):
    if request.method == "GET":
        #Query from the category table to get category name    
        categories = Category.objects.all()
        ctx = {"page": "blog", "categories":categories}
        return render(request, "blogs/view_blog.html", ctx)

    elif request.method == "POST":
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

@login_required
def blog(request, cat_id):
    if request.method == "GET":
        category = Category.objects.get(id=cat_id)
        blogs = Blog.objects.filter(author=request.team.user, category=category)

        ctx = {
            "category": category,
            "blogs": blogs
        }

        return render(request, "blogs/blog.html", ctx)

    elif request.method == "POST":
        form = CreateBlogForm(request.POST)
        if form.is_valid():
            title = request.POST['title']
            blog = form.cleaned_data['body']
            category = Category.objects.get(id=cat_id)
            author = request.user
            created_date = timezone.now()
            blog = Blog(title=title, body=blog,category=category,created_date=created_date, author=author)
            blog.save()

            return redirect("hc-blog")

    ctx = {"page": "blog", "form": form, "id": cat_id}
    return render(request, "blogs/add_blog.html", ctx)

def send_blog_link(self, blog_id, inviting_profile=None):
    path = reverse("hc-single-blog", kwargs={'blog_id':blog_id})
    ctx = {
        "blog_link": settings.SITE_ROOT + path,
        "inviting_profile": inviting_profile,
    }
    emails.share_blog(self, ctx, blog_id)

def view_blogs(request):
    q = Blog.objects.filter(author=request.team.user)
    blogs = list(q)
    categories = Category.objects.all()        
    ctx = {
        "page": "blogs",
        "blogs": blogs,
        "categories": categories
    }

    return render(request, "blogs/view_blog.html", ctx)

def single_blog(request, blog_id):
    if request.method == "POST":
        if "share-blog" in request.POST:
            form = ShareBlogForm(request.POST)
            if form.is_valid():
                # send an email
                email = form.cleaned_data["email"]

            send_blog_link(email, blog_id)
            messages.success(request, "Blog link shared to %s" % email)
    else:
        blog = Blog.objects.get(id=blog_id)
        blog.delete()
        messages.info(request, "Blog deleted!")
        return redirect("hc-blog")

    ctx = {
        "blog": blog,
        "id": blog_id
    } 
    return render(request, "blogs/single_blog.html", ctx)

def delete_category(request, cat_id):
    category = Category.objects.get(id=cat_id)
    category.delete()
    messages.info(request, "Category deleted!")
    return redirect("hc-blog")

