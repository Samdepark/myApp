from django.urls import path
from .views import (
    ItemDetailView,
    CheckoutView,
    HomeView,
    add_to_cart,
    remove_from_cart,
    OrderSummaryView,
    remove_single_item_from_cart
    )


app_name = 'Authentication'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('products/<slug>/', ItemDetailView.as_view(), name='products'),
    path('add-to-cart/<slug>/', add_to_cart, name='AddToCart'),
    path('remove-from-cart/<slug>/', remove_from_cart, name='RemoveFromCart'),
    path('remove-item-from-cart/<slug>/', remove_single_item_from_cart, name='RemoveItemFromCart'),
    path('order-summary', OrderSummaryView.as_view(), name='order-summary'),
    path('checkOut/', CheckoutView.as_view(), name='checkout')
]