from django.contrib import admin
from .models import Category, IMG, Blog

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

@admin.register(IMG)
class IMGAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'author', 'get_read_num', 'publish_time', 'last_updated_time')