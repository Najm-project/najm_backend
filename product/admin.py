from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import CategoryModel, ColorModel, Attribute, AttributeCategory, ProductModel, ProductImageModel
from django.utils.html import format_html, format_html_join


@admin.register(CategoryModel)
class CategoryModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'products', 'slug')
    search_fields = ('name',)

    def products(self, obj):
        return obj.products.count()

    products.short_description = 'Товары'


class ProductImageInline(admin.TabularInline):
    model = ProductImageModel
    extra = 1


class ColorModelInline(admin.TabularInline):
    model = ColorModel
    extra = 1


class AttributeInline(admin.TabularInline):
    model = Attribute
    extra = 1


class AttributeCategoryInline(admin.TabularInline):
    model = AttributeCategory
    extra = 1


@admin.register(ProductModel)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'in_stock', 'is_recommended', 'category', 'slug')
    search_fields = ('name', 'category__name',)
    list_filter = ('category', 'is_recommended', 'in_stock')
    inlines = [ProductImageInline, ColorModelInline, AttributeCategoryInline, AttributeInline]


@admin.register(ProductImageModel)
class ProductImageModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'image')
    search_fields = ('product__name',)
    list_filter = ('product__name',)


@admin.register(ColorModel)
class ColorModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'product_image_id', 'product', 'in_stock', 'slug')
    search_fields = ('name',)


@admin.register(Attribute)
class AttributeAdmin(admin.ModelAdmin):
    list_display = ('name', 'in_stock', 'product', 'slug')
    search_fields = ('name', 'attribute_category__name')
    list_filter = ('attribute_category',)


@admin.register(AttributeCategory)
class AttributeCategoryModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'product', 'slug')
    search_fields = ('name', 'product__name')
