from rest_framework import serializers
from .models import ProductModel, ProductImageModel, CategoryModel, ColorModel, Attribute


class CategorySerializer(serializers.ModelSerializer):
    product_count = serializers.SerializerMethodField()

    class Meta:
        model = CategoryModel
        fields = ['id', 'name', 'slug', 'product_count']

    def get_product_count(self, obj):
        return obj.products.count()


class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = ColorModel
        fields = ['id', 'name', 'product', 'slug']


class AttributeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attribute
        fields = ['id', 'name', 'attribute_category', 'slug']


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImageModel
        fields = ['id', 'image', 'product']


class ProductSerializer(serializers.ModelSerializer):
    images = ProductImageSerializer(many=True, read_only=True)
    category = CategorySerializer(read_only=True)
    color = ColorSerializer(read_only=True, many=True)
    attribute = AttributeSerializer(read_only=True, many=True)

    class Meta:
        model = ProductModel
        fields = ['id', 'name', 'price', 'description', 'in_stock', 'is_recommended', 'color', 'attribute', 'category',
                  'images', 'slug']
