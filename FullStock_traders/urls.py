from django.contrib import admin;
from django.urls import path, include;

urlpatterns = [
    path('admin/', admin.site.urls),
    path('products/', include('Products.url')),
    path('shopping_cart/', include('Shopping_Cart.url')),
    path('ratings/', include('Ratings.url')),
]
