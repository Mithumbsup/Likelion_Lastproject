from django.contrib import admin
from .models import Post, Comment, Order

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Order)
# Register your models here.