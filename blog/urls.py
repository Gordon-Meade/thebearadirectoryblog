
from django.urls import path
from . import views

# Urls for blog app

urlpatterns = [
    path("", views.blog_index, name="blog_index"),
    path("post/<int:pk>/", views.blog_detail, name="blog_detail"),
    path("category/<category>/", views.blog_category, name="blog_category"),
    path("blog_info/", views.info_view, name="blog_info"),
    path("index/", views.blog_index, name="blog_index"),
]