from django.urls import path
from .views import *
from .myview.business import UserProfile
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView, # Optional, for verifying a token's validity
)

urlpatterns = [
    path('', UserRegistrationView.as_view(), name='index'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),

    # Get the profile about user
    path('profile/<int:user_id>/', UserProfile.as_view(), name='user-profile'),
    
    # Password reseting
    path('password-reseting/', PasswordResetRequestView.as_view(), name="password-reseting"),
    path('password-reset/confirm/', PasswordResetConfirmView.as_view(), name='password-reset-confirm'),
    path('password-reset/verify-token/', PasswordResetTokenVerifyView.as_view(), name='verify-token'),
    
    # JWT Authentication Endpoints
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'), # Optional
]