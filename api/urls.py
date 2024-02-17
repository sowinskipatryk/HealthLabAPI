from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from . import views

urlpatterns = [
    path('api/login/', TokenObtainPairView.as_view(), name='login'),
    path('api/refresh/', TokenRefreshView.as_view(), name='refresh'),
    path('api/patients/', views.PatientListView.as_view(), name='patients'),
    path('api/patients/<int:pk>/', views.PatientDetailView.as_view(), name='patient-details'),
    path('api/orders/', views.OrderListView.as_view(), name='orders'),
    path('api/orders/<int:pk>/', views.OrderDetailView.as_view(), name='order-details'),
    path('api/results/', views.ResultListView.as_view(), name='results'),
    path('api/results/<int:pk>/', views.ResultDetailView.as_view(), name='result-details'),
    path('api/patient_profile/<int:id>/', views.get_patient_page, name='patient-profile'),
]
