from django.contrib import admin
from .models import Post, Category


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['author', 'category', 'status']
    list_filter = ['status']
    search_fields = ['title', 'content']
    raw_id_fields = ['author', 'category']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']
