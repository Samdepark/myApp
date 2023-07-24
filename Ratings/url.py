from django.urls import path;
from . import views;

urlpatterns =[
    path("ratings/", views.index , name ='ratings')
]