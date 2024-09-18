from django.contrib import admin

# Register your models here.
from .models import Category, Product

# For Categories
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_diplay = ["name", "slug"]
    prepopulated_fields = {'slug': ('name',)}

# For Products
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["name", "price", "available", "created", "updated", "category"]
    prepopulated_fields = {'slug': ('name',)}
