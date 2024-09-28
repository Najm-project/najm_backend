from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView, TokenVerifyView, TokenObtainPairView

from .views import UserRegistrationView, VerifyCodeView, UpdateNameView, ChangePasswordView, \
    RequestPasswordResetView, ResendVerificationCodeView

app_name = 'user'

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('verify/', VerifyCodeView.as_view(), name='verify'),

    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('login/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('login/token/verify/', TokenVerifyView.as_view(), name='token_verify'),

    path('update-name/', UpdateNameView.as_view(), name='update-name'),
    path('change-password/', ChangePasswordView.as_view(), name='change-password'),

    path('request-password-reset/', RequestPasswordResetView.as_view(), name='request-password-reset'),
    path('resend-verification-code/', ResendVerificationCodeView.as_view(), name='resend-verification-code'),
]
