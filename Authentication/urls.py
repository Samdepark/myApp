from django.urls import path
from .views import Registerview, Loginview, Userview, Logoutview


app_name = 'Authentication'

urlpatterns =[
    path('signup/', Registerview.as_view()),
    path('SignIn/',Loginview.as_view()),
    path('user/',Userview.as_view()),
    path('signOut/', Logoutview.as_view())
]