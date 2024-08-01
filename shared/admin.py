from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import CartItem, FavoriteItem, Review


@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'quantity', 'created_at', 'updated_at')
    search_fields = ('user__username', 'product__name')
    list_filter = ('created_at', 'updated_at')
    ordering = ('-created_at',)


@admin.register(FavoriteItem)
class FavoriteItemAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'created_at', 'updated_at')
    search_fields = ('user__username', 'product__name')
    list_filter = ('created_at', 'updated_at')
    ordering = ('-created_at',)


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'rating', 'comment', 'created_at', 'updated_at')
    search_fields = ('user__username', 'product__name')
    list_filter = ('rating', 'created_at', 'updated_at')
    ordering = ('-created_at',)
