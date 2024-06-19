from . import views
from django.urls import path

urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('blog/', views.PostList.as_view(), name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact_view, name='contact'),
    path('post/<slug:slug>/', views.post_detail, name="post_detail"),
    path('post/<slug:slug>/edit_comment/<int:comment_id>', views.comment_edit, name='comment_edit'),
    path('post/<slug:slug>/delete_comment/<int:comment_id>', views.comment_delete, name='comment_delete'),
]
