from rest_framework import generics, permissions
from rest_framework.permissions import IsAuthenticated, AllowAny

from .models import CartItem, FavoriteItem, Review, OrderModel
from .serializers import CartItemSerializer, FavoriteItemSerializer, ReviewSerializer, BuyProductSerializer


class CartItemListCreateView(generics.ListCreateAPIView):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class CartItemRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer
    permission_classes = [permissions.IsAuthenticated]


# FavoriteItem Views
class FavoriteItemListCreateView(generics.ListCreateAPIView):
    queryset = FavoriteItem.objects.all()
    serializer_class = FavoriteItemSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class FavoriteItemRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = FavoriteItem.objects.all()
    serializer_class = FavoriteItemSerializer
    permission_classes = [permissions.IsAuthenticated]


# Review Views
class ReviewListCreateView(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ReviewRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticated]


class BuyProductView(generics.CreateAPIView):
    queryset = OrderModel.objects.all()
    serializer_class = BuyProductSerializer

    def get_permissions(self):
        if self.request.user.is_authenticated:
            return [IsAuthenticated()]
        return [AllowAny()]
