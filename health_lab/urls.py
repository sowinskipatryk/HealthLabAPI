from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', SpectacularSwaggerView.as_view(), name='doc'),
    path('redoc/', SpectacularRedocView.as_view(), name='redoc'),
    path('schema/', SpectacularAPIView.as_view(), name='schema'),

    path('api/', include('api.urls'))
]
