from django.contrib import admin
from .models import Post
# Register your models here.

# admin panelinden postlara erişmek için 
admin.site.register(Post)