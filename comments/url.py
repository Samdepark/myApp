from django.urls import path;
from . import views;

urlpatterns =[
    path('comments/', views.index, name = 'comments')
]