from django.contrib import admin
from .models import BlogPost, Category


# Register your models here.
admin.site.register(Category)
admin.site.register(BlogPost)
