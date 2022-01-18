from django.urls import path
from .views import ProductListView, ProductDetailView, create_product

urlpatterns = [
    path('', ProductListView.as_view(), name='product_list'),
    path('products/create', create_product, name='product_create'),
    path('<uuid:pk>', ProductDetailView.as_view(), name='product_detail'),
]
