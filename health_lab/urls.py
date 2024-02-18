from django.contrib import admin
from django.shortcuts import redirect
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', lambda request: redirect('doc')),
    path('api/', include('api.urls'))
]
