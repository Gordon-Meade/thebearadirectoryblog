from . import views
from django.urls import path

handler404 = 'blog1.views.custom_404'

urlpatterns = [
    path('blog/', views.PostList.as_view(), name='home'),
    path('about/', views.about, name='about'),
    path('', views.welcome, name='welcome'),
    path('<slug:slug>/', views.post_detail, name="post_detail"),
    path('<slug:slug>/edit_comment/<int:comment_id>',
         views.comment_edit, name='comment_edit'),
    path('<slug:slug>/delete_comment/<int:comment_id>',
         views.comment_delete, name='comment_delete'),
    
]