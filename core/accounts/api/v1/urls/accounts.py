from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView, TokenVerifyView
from .. import views

urlpatterns = [
    path('register/', views.RegisterApiView.as_view(), name='register'),
    path('login/', views.CustomObtainAuthToken.as_view(), name='login'),
    path('logout/', views.LogoutApiView.as_view(), name='logout'),
    path('jwt/create/', views.CustomTokenObtainPairView.as_view(), name='jwt-create'),
    path('jwt/refresh/', TokenRefreshView.as_view(), name='jwt-refresh'),
    path('jwt/verify/', TokenVerifyView.as_view(), name='jwt-verify'),
    path('password-change/', views.ChangePasswordApiView.as_view(), name='password-change'),
    # path('activation/confirm/', views.ChangePasswordApiView.as_view(), name='activation-confirm'),
    # path('activation/resend/', views.ChangePasswordApiView.as_view(), name='activation-resend'),
    path('test-email/', views.TestEmailApiView.as_view(), name='test-email'),
]
