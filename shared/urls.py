from django.urls import path, include

from shared.views import CartItemListCreateView, CartItemRetrieveUpdateDestroyView, FavoriteItemListCreateView, \
    FavoriteItemRetrieveUpdateDestroyView, ReviewListCreateView, ReviewRetrieveUpdateDestroyView

app_name = 'shared'

urlpatterns = [
    path('cart-items/', CartItemListCreateView.as_view(), name='cartitem-list-create'),
    path('cart-items/<int:pk>/', CartItemRetrieveUpdateDestroyView.as_view(), name='cartitem-detail'),

    path('favorite-items/', FavoriteItemListCreateView.as_view(), name='favoriteitem-list-create'),
    path('favorite-items/<int:pk>/', FavoriteItemRetrieveUpdateDestroyView.as_view(), name='favoriteitem-detail'),

    path('reviews/', ReviewListCreateView.as_view(), name='review-list-create'),
    path('reviews/<int:pk>/', ReviewRetrieveUpdateDestroyView.as_view(), name='review-detail'),
]
