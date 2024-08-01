from django.urls import path
from .views import ProductListView, RecommendedProductListView, NewProductListView, ProductByCategoryView, \
    CategoryListView, PensProductListView, NotebooksProductListView, DiariesProductListView, StickersProductListView

app_name = 'product'

urlpatterns = [
    path('all-products/', ProductListView.as_view(), name='all-products'),
    path('recommended-products/', RecommendedProductListView.as_view(), name='recommended-products'),
    path('new-products/', NewProductListView.as_view(), name='new-products'),
    path('categories/', CategoryListView.as_view(), name='categories'),
    path('categories/<str:category_name>/', ProductByCategoryView.as_view(), name='products-by-category'),
    path('pens/', PensProductListView.as_view(), name='pens-products'),
    path('notebooks/', NotebooksProductListView.as_view(), name='notebooks-products'),
    path('diaries/', DiariesProductListView.as_view(), name='diaries-products'),
    path('stickers/', StickersProductListView.as_view(), name='stickers-products'),
]