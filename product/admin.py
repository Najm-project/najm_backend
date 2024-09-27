from django.contrib import admin
from .models import CategoryModel, ColorModel, Attribute, AttributeCategory, ProductModel, ProductImageModel


@admin.register(CategoryModel)
class CategoryModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'updated_at')
    search_fields = ('name',)
    ordering = ('name',)
    exclude = ('slug',)


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
    list_display = ('name', 'price', 'in_stock', 'is_recommended', 'category', 'color', 'created_at', 'updated_at')
    search_fields = ('name', 'category__name', 'color__name')
    list_filter = ('category', 'color', 'is_recommended', 'in_stock')
    ordering = ('name',)
    exclude = ('slug',)
    inlines = [ProductImageInline]


@admin.register(ProductImageModel)
class ProductImageModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'image', 'created_at', 'updated_at')
    search_fields = ('product__name',)
    ordering = ('product',)


@admin.register(ColorModel)
class ColorModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'updated_at')
    search_fields = ('name',)
    ordering = ('name',)
    exclude = ('slug',)

@admin.register(Attribute)
class AttributeAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'created_at', 'updated_at')
    search_fields = ('name', 'attribute_category__name')
    list_filter = ('category',)
    ordering = ('name',)
    exclude = ('slug',)


@admin.register(AttributeCategory)
class AttributeCategoryModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'product', 'created_at', 'updated_at')
    search_fields = ('name', 'product__name')
    ordering = ('name',)
    exclude = ('slug',)
