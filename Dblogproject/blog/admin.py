from django.contrib import admin
from blog.models import Blog
from .models import Blog, Comment, HashTag

# Register your models here.

admin.site.register(Blog)
admin.site.register(Comment)
admin.site.register(HashTag)