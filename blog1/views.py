from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import NewPost, Comment, ContactForm
from .forms import CommentForm, ContactForm


# custom 404 view
def custom_404(request, exception):
    return render(request, 'blog1/404.html', status=404)

# custom 500 view
def custom_500(request):
    return render(request, 'blog1/500.html')

# Blog post 
class PostList(generic.ListView):
    queryset = NewPost.objects.filter(status=1)
    template_name = "blog1/blog.html"
    paginate_by = 6
    context_object_name = 'post_list'

# Blog Detail
def post_detail(request, slug):
    queryset = NewPost.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comments = post.comments.all().order_by("-created_on")
    comment_count = post.comments.filter(approved=True).count()
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
    else:
        comment_form = CommentForm()

    return render(
        request,
        "blog1/post_detail.html",
        {
            "post": post,
            "comments": comments,
            "comment_count": comment_count,
            "comment_form": comment_form
        },
    )

# Comment Edit
def comment_edit(request, slug, comment_id):
    queryset = NewPost.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id)

    if request.method == "POST":
        comment_form = CommentForm(data=request.POST, instance=comment)
        if comment_form.is_valid() and comment.name == request.user.username:
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.approved = False  # Re-approval needed after edit
            comment.save()
            messages.add_message(request, messages.SUCCESS, 'Comment updated!')
            return HttpResponseRedirect(reverse('post_detail', args=[slug]))
        else:
            messages.add_message(request, messages.ERROR, 'Error updating comment!')
            return render(request, 'blog1/comment_form.html', {'form': comment_form})
    else:
        comment_form = CommentForm(instance=comment)
        return render(request, 'blog1/comment_form.html', {'form': comment_form})

# Comment Delete
def comment_delete(request, slug, comment_id):
    queryset = NewPost.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id)

    if request.method == "POST":
        if comment.name == request.user.username:
            comment.delete()
            messages.add_message(request, messages.SUCCESS, 'Comment deleted!')
        else:
            messages.add_message(request, messages.ERROR, 'You can only delete your own comments!')
        return HttpResponseRedirect(reverse('post_detail', args=[slug]))
    
    return render(request, 'blog1/comment_confirm_delete.html', {'comment': comment, 'post': post})
 
# About Page
def about(request):
    return render(request, 'blog1/about.html')

# Welcome Page
def welcome(request):
    return render(request, 'blog1/welcome.html')

# Blog Page
def blog(request):
    return render(request, 'blog1/blog.html')


def contact_form_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()  # Save the form data to the database
            return redirect('success')  # Redirect to success page
    else:
        form = ContactForm()
    return render(request, 'blog1/contact.html', {'form': form})

def success_view(request):
    return render(request, 'blog1/success.html')