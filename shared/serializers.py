from rest_framework import serializers
from .models import CartItem, FavoriteItem, Review, OrderModel
from rest_framework.exceptions import ValidationError


class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = ['id', 'user', 'product', 'quantity', 'created_at', 'updated_at']


class FavoriteItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = FavoriteItem
        fields = ['id', 'user', 'product', 'created_at', 'updated_at']


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'user', 'product', 'rating', 'comment', 'created_at', 'updated_at']


class BuyProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderModel
        fields = ['product', 'quantity', 'color', 'attributes', 'first_name', 'last_name', 'phone_number',
                  'delivery_type']
        extra_kwargs = {
            'first_name': {'required': False},
            'last_name': {'required': False},
            'phone_number': {'required': False}
        }

    def validate(self, data):
        user = self.context['request'].user
        if not user.is_authenticated:
            if not data.get('first_name') or not data.get('last_name') or not data.get('phone_number'):
                raise ValidationError("First name, last name, and phone number are required for unauthenticated users.")
        return data

    def create(self, validated_data):
        user = self.context['request'].user
        if user.is_authenticated:
            validated_data['first_name'] = user.first_name
            validated_data['last_name'] = user.last_name
            validated_data['phone_number'] = user.phone_number
        return super().create(validated_data)


class BuyProductsSerializer(serializers.ModelSerializer):
    cart_items = serializers.PrimaryKeyRelatedField(many=True, queryset=CartItem.objects.all())

    class Meta:
        model = OrderModel
        fields = ['cart_items', 'first_name', 'last_name', 'phone_number',
                  'delivery_type']
        extra_kwargs = {
            'first_name': {'required': False},
            'last_name': {'required': False},
            'phone_number': {'required': False}
        }

    def validate(self, data):
        user = self.context['request'].user
        if not user.is_authenticated:
            if not data.get('first_name') or not data.get('last_name') or not data.get('phone_number'):
                raise ValidationError("First name, last name, and phone number are required for unauthenticated users.")
        return data
