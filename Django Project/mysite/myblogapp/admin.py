from django.contrib import admin

# Register your models here.
from .models import BlogEntry,Comment

admin.site.register(BlogEntry)
admin.site.register(Comment)