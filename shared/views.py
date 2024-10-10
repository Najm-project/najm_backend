from django.template.defaultfilters import first
from rest_framework import generics, permissions
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED

from .models import CartItem, FavoriteItem, Review, OrderModel
from .serializers import CartItemSerializer, FavoriteItemSerializer, ReviewSerializer, BuyProductSerializer, \
    BuyProductsSerializer


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


class BuyProductsView(generics.GenericAPIView):
    serializer_class = BuyProductsSerializer

    def get_permissions(self):
        if self.request.user.is_authenticated:
            return [IsAuthenticated()]
        return [AllowAny()]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.data
        cart_items = data['cart_items']
        user = self.request.user
        if user.is_authenticated:
            first_name = user.first_name
            last_name = user.last_name
            phone_number = user.phone_number
        else:
            first_name = request.data['first_name']
            last_name = request.data['last_name']
            phone_number = request.data['phone_number']

        for cart_item in cart_items:
            OrderModel.objects.create(
                first_name=first_name,
                last_name=last_name,
                phone_number=phone_number,
                delivery_type=data['delivery_type'],
                product_id=cart_item['product_id'],
                quantity=cart_item['quantity'],
                color=cart_item['color'],
                attributes=cart_item['attributes'],
            )

        return Response(status=HTTP_201_CREATED)
