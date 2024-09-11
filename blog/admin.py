from django.contrib import admin

from blog.models import Post, Comment, Category, Tag

# Register your models here.
admin.site.register(Post)
admin.site.register(Tag)
admin.site.register(Comment)
admin.site.register(Category)
