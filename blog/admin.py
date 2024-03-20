from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from blog.models import Category, Comment, Post

class CategoryAdmin(admin.ModelAdmin):
    pass

class PostAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)

class CommentAdmin(admin.ModelAdmin):
    pass




admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)