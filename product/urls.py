from django.urls import path
from .views import ProductListView, RecommendedProductListView, NewProductListView, ProductByCategoryView, \
    CategoryListView

app_name = 'product'

urlpatterns = [
    path('all-products/', ProductListView.as_view(), name='all-products'),
    path('best-sellers/', RecommendedProductListView.as_view(), name='recommended-products'),
    path('new-products/', NewProductListView.as_view(), name='new-products'),
    path('categories/', CategoryListView.as_view(), name='categories'),  #----
    path('categories/<int:category_id>/', ProductByCategoryView.as_view(), name='products-by-category'),   #----
]