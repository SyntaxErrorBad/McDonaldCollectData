from django.urls import path

from .views import StartScrapingAPIView
from .views import AllProductsAPIView, ProductByNameAPIView, ProductByNameFieldAPIView

app_name = 'api'

urlpatterns = [
    path('start-scraping/', StartScrapingAPIView.as_view(), name="start-scraping-site"),
    path('all-products/', AllProductsAPIView.as_view(), name="all-products"),
    path('products/<str:product_name>/', ProductByNameAPIView.as_view(), name="product-by-name"),
    path('products/<str:product_name>/<str:product_field>/', ProductByNameFieldAPIView.as_view(), name="product-by-name")
]
