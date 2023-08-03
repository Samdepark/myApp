from django.contrib import admin;
from django.urls import path, include;


app_name = 'FullStock_traders'


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('Authentication.url')),
    path('products/', include('Products.url')),
    path('shopping_cart/', include('Shopping_Cart.url')),
    path('ratings/', include('Ratings.url')),
]
