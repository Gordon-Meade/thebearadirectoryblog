from django.shortcuts import render, get_object_or_404
from blog.models import Post, Comment

def blog_index(request):
    posts = Post.objects.all().order_by("-created_on")
    for post in posts:
        # featured_image in Cloudinary
        post.featured_image_url = post.featured_image.url 
    context = {

        "posts": posts,
    }
    return render(request, "blog/index.html", context)

def blog_category(request, category):
    posts = Post.objects.filter(
        categories__name__contains=category
    ).order_by("-created_on")
    context = {
        "category": category,
        "posts": posts,
    }
    return render(request, "blog/category.html", context)

def blog_detail(request, pk):
    post = Post.objects.get(pk=pk)
    comments = Comment.objects.filter(post=post)
    post.featured_image_url = post.featured_image.url
    context = {
        "post": post,
        "comments": comments,
    }
    return render(request, "blog/detail.html", context)
