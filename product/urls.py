from django.urls import path

from .views import TagListAPIView, ProductListAPIView

urlpatterns = [
    path('tags/', TagListAPIView.as_view(), name='tag'),
    path('products/popular/', ProductListAPIView.as_view(), name='products_popular'),
    path('products/limited/', ProductListAPIView.as_view(), name='products_limited'),
    path('products/banners/', ProductListAPIView.as_view(), name='products_banners'),
]
