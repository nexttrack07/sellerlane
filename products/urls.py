from django.urls import path
from .views import ProductCreateView, ProductListView, ProductDetailView, ProductPhotoDeleteView, ProductUpdateView, ProductDeleteView

urlpatterns = [
    path('', ProductListView.as_view(), name='product_list'),
    path('products/create', ProductCreateView.as_view(), name='product_create'),
    path('<uuid:pk>', ProductDetailView.as_view(), name='product_detail'),
    path('<int:pk>/delete-photo', ProductPhotoDeleteView.as_view(), name='product_photo_delete'),
    path('<uuid:pk>/update', ProductUpdateView.as_view(), name='product_update'),
    path('<uuid:pk>/delete', ProductDeleteView.as_view(), name='product_delete'),
]
