from rest_framework import generics
from .models import ProductModel, CategoryModel
from .serializers import ProductSerializer, CategorySerializer


class ProductListView(generics.ListAPIView):
    queryset = ProductModel.objects.all()
    serializer_class = ProductSerializer


class RecommendedProductListView(generics.ListAPIView):
    queryset = ProductModel.objects.filter(is_recommended=True)
    serializer_class = ProductSerializer


class PensProductListView(generics.ListAPIView):
    queryset = ProductModel.objects.filter(
        category__name__in=['pen', 'pens', 'pencil', 'pencils', 'карандаш', 'карандаши', 'ручка', 'ручки'])
    serializer_class = ProductSerializer


class DiariesProductListView(generics.ListAPIView):
    queryset = ProductModel.objects.filter(
        category__name__in=['diary', 'diaries', 'ежедневник', 'ежедневники'])
    serializer_class = ProductSerializer


class NotebooksProductListView(generics.ListAPIView):
    queryset = ProductModel.objects.filter(
        category__name__in=['notebook', 'notebooks', 'тетрадь', 'тетради'])
    serializer_class = ProductSerializer


class StickersProductListView(generics.ListAPIView):
    queryset = ProductModel.objects.filter(
        category__name__in=['sticker', 'stickers', 'стикер', 'стикеры'])
    serializer_class = ProductSerializer


class NewProductListView(generics.ListAPIView):
    queryset = ProductModel.objects.order_by('-created_at')[:10]
    serializer_class = ProductSerializer


class ProductByCategoryView(generics.ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        category_name = self.kwargs['category_name']
        return ProductModel.objects.filter(category__name=category_name)


class CategoryListView(generics.ListAPIView):
    queryset = CategoryModel.objects.all()
    serializer_class = CategorySerializer
