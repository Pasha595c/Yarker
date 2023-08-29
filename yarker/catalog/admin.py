from django.contrib import admin
from .forms import CategoryForm, ProductForm
from .models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "image")


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    form = ProductForm
    list_display = (
        "name",
        "price",
        "category",
        "image",
        "slug",
    )
    list_filter = ("category",)
