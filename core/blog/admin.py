from django.contrib import admin
from .models import Post, Category
from .actions import make_activation, make_deactivation


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['author', 'category', 'status']
    list_filter = ['status']
    search_fields = ['title', 'content']
    raw_id_fields = ['author', 'category']
    list_editable = ['status']
    actions = [make_activation, make_deactivation]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']
