"""usersAPI URL Configuration
"""
from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from users.api.views import ObtainTokenPairView, RegisterUserView

app_name = 'users'

urlpatterns = [
    path('login/', ObtainTokenPairView.as_view(), name='login'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegisterUserView.as_view(), name='register'),
]
