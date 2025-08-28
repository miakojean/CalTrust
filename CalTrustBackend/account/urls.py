from django.urls import path
from .views import *
from .myview.business import UserProfile, FirmProfileView
from .myview.customer import CustomerProfileView, CompaniesList
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

urlpatterns = [
    path('', UserRegistrationView.as_view(), name='index'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),

    # Customer endpoints
    path('customer/profile/', CustomerProfileView.as_view(), name='customer-profile'),
    path('customer/companies/', CompaniesList.as_view(), name='customer-companies'),
    
    # Firm endpoints
    path('firm/profile/', FirmProfileView.as_view(), name='firm-profile'),
    
    # Public profile view
    path('profile/<int:user_id>/', UserProfile.as_view(), name='user-profile'),
    
    # Password reset
    path('password-reseting/', PasswordResetRequestView.as_view(), name="password-reseting"),
    path('password-reset/confirm/', PasswordResetConfirmView.as_view(), name='password-reset-confirm'),
    path('password-reset/verify-token/', PasswordResetTokenVerifyView.as_view(), name='verify-token'),
    
    # JWT Authentication
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]