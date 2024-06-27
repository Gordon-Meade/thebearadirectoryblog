from django.urls import path
from . import views

urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('blog/', views.PostList.as_view(), name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact_form_view, name='contact'),
    path('success/', views.success_view, name='success'),
    path('post/<slug:slug>/', views.post_detail, name="post_detail"),
    path('post/<slug:slug>/edit_comment/<int:comment_id>/', views.comment_edit, name='comment_edit'),
    path('post/<slug:slug>/delete_comment/<int:comment_id>/', views.comment_delete, name='comment_delete'),
]
