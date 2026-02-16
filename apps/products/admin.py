from django.contrib import admin
from products.models import Category, Product

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'created_at')
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name',)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'price', 'image', 'description', 'stock', 'is_active', 'created_at',)
    list_filter=('is_active',)
    prepopulated_fields = {'slug': ('name',)}
    search_fields =('name',)