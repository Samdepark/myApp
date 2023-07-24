from django.urls import path;
from . import views;

urlpatterns = [
    path("shopping_cart/", views.index, name= 'shopping_cart')
]