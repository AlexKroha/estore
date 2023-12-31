from django.contrib import admin
from .models import Category, Product


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}
admin.site.register(Category, CategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'slug', 'price', 'stock', 'available', 'portfolio', 'created', 'updated']
    list_filter = ['category','available', 'created', 'updated']
    list_editable = ['price', 'stock', 'available', 'portfolio']
    prepopulated_fields = {'slug': ('name',)}
admin.site.register(Product, ProductAdmin)