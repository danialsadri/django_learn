from django.urls import path
from .import views
from rest_framework_simplejwt.views import TokenRefreshView, TokenVerifyView


app_name = 'api-v1'
urlpatterns = [
    path('register/', views.RegisterApiView.as_view(), name='register'),
    path('login/', views.CustomObtainAuthToken.as_view(), name='login'),
    path('logout/', views.LogoutApiView.as_view(), name='logout'),
    path('jwt/create/', views.CustomTokenObtainPairView.as_view(), name='jwt-create'),
    path('jwt/refresh/', TokenRefreshView.as_view(), name='jwt-refresh'),
    path('jwt/verify/', TokenVerifyView.as_view(), name='jwt-verify'),
    path('password-change/', views.ChangePasswordApiView.as_view(), name='password-change'),
]
