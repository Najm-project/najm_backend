from django.contrib import admin
from .models import CategoryModel, ColorModel, Attribute, ProductModel, ProductImageModel


@admin.register(CategoryModel)
class CategoryModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'updated_at')
    search_fields = ('name',)
    ordering = ('name',)


@admin.register(ColorModel)
class ColorModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'updated_at')
    search_fields = ('name',)
    ordering = ('name',)


@admin.register(Attribute)
class AttributeAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'created_at', 'updated_at')
    search_fields = ('name', 'category__name')
    list_filter = ('category',)
    ordering = ('name',)


class ProductImageInline(admin.TabularInline):
    model = ProductImageModel
    extra = 1


@admin.register(ProductModel)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'in_stock', 'is_recommended', 'category', 'color', 'created_at', 'updated_at')
    search_fields = ('name', 'category__name', 'color__name')
    list_filter = ('category', 'color', 'is_recommended', 'in_stock')
    ordering = ('name',)
    inlines = [ProductImageInline]


@admin.register(ProductImageModel)
class ProductImageModelAdmin(admin.ModelAdmin):
    list_display = ('product', 'image', 'created_at', 'updated_at')
    search_fields = ('product__name',)
    ordering = ('product',)
