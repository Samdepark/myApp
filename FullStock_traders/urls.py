from django.urls import path,include;
from django.conf import settings
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView


app_name = 'FullStock_traders'


urlpatterns = [
    # path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),#used for all sign up and logins
    path('api/', include('Authentication.urls')),#connection with the Authentication urls

    path('api/schema/', SpectacularAPIView.as_view(), name="schema"),
    path('api/schema/docs/',SpectacularSwaggerView.as_view(url_name="schema") ),
]
