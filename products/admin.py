from django.contrib import admin
from .models import Product, Category

# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "sku",
        "name",
        "category",
        "price",
        "is_organic",
        "origin",
        "image",
    )

    ordering = ("name",)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        "friendly_name",
        "name",
        "cat_image",
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
