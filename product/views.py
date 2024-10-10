from rest_framework import generics
from .models import ProductModel, CategoryModel
from .serializers import ProductSerializer, CategorySerializer


class ProductListView(generics.ListAPIView):
    queryset = ProductModel.objects.all()
    serializer_class = ProductSerializer


class RecommendedProductListView(generics.ListAPIView):
    queryset = ProductModel.objects.filter(is_recommended=True)
    serializer_class = ProductSerializer


class NewProductListView(generics.ListAPIView):
    queryset = ProductModel.objects.order_by('-created_at')[:10]
    serializer_class = ProductSerializer


class ProductByCategoryView(generics.ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        category_id = self.kwargs['category_id']
        return ProductModel.objects.filter(category_id=category_id)


class CategoryListView(generics.ListAPIView):
    queryset = CategoryModel.objects.all()
    serializer_class = CategorySerializer
