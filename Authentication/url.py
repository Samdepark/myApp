from django.urls import path
from Authentication import views

app_name = 'Authentication'

urlpatterns =[
    path('', views.Register, name='Register'),
]