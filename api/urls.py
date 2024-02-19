from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .views import *


urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('refresh/', TokenRefreshView.as_view(), name='refresh'),

    path('patients/', PatientListView.as_view(), name='patients'),
    path('patients/<int:pk>/', PatientDetailView.as_view(), name='patient-details'),
    path('patients/<int:pk>/update/', PatientUpdateView.as_view(), name='patient-update'),
    path('patients/<int:pk>/delete/', PatientDeleteView.as_view(), name='patient-delete'),

    path('orders/', OrderListView.as_view(), name='orders'),
    path('orders/<int:pk>/', OrderDetailView.as_view(), name='order-details'),
    path('orders/<int:pk>/update/', OrderUpdateView.as_view(), name='order-update'),
    path('orders/<int:pk>/delete/', OrderDeleteView.as_view(), name='order-delete'),

    path('results/', ResultListView.as_view(), name='results'),
    path('results/<int:pk>/', ResultDetailView.as_view(), name='result-details'),
    path('results/<int:pk>/update/', ResultUpdateView.as_view(), name='result-update'),
    path('results/<int:pk>/delete/', ResultDeleteView.as_view(), name='result-delete'),

    path('patient_profile/<int:pk>/', PatientProfileDetailView.as_view(), name='patient-profile'),
]
