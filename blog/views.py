from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.contrib import messages
from blog.models import Post, Comment
from .forms import CommentForm

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

def blog_detail(request, pk,):
    post = Post.objects.get(pk=pk)
    comments = Comment.objects.filter(post=post)
    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
    messages.add_message(
        request, messages.SUCCESS,
        'Comment submitted and awaiting approval'
    )

    comment_form = CommentForm()
    post.featured_image_url = post.featured_image.url
    context = {
        "post": post,
        "comments": comments,
        "comment_form": comment_form,
    }
    return render(request, "blog/detail.html", context)
