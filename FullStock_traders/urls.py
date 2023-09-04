from django.contrib import admin;
from django.urls import path,include;
from django.conf import settings


app_name = 'FullStock_traders'


urlpatterns = [
    # path('admin/', admin.site.urls),
    path('api/', include('Authentication.urls')),
]
