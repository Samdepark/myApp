from django.contrib import admin;
from django.urls import path, include;

urlpatterns = [
    path('admin/', admin.site.urls),
    path('products/', include('products.urls')),
    path('shopping_cart/', include('Shopping_Cart.urls')),
    path('ratings/', include('Ratings.url')),
]
