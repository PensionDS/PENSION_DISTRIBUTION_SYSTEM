from django.urls import path
from .views import (PensionUserRegister,PensionUserActivation, TokenGenerationView,
    Home, PensionUserChangePassword, PensionResendOTP
    )


urlpatterns = [
    path('user-register/', PensionUserRegister.as_view(), name = 'user-register'),
    path('resend-otp/', PensionResendOTP.as_view(), name = 'resend-otp'),
    path('user-activation/', PensionUserActivation.as_view(), name = 'user-activation'),
    path('token-genration/', TokenGenerationView.as_view(), name='token_obtain_pair'),   
    path('home/', Home.as_view() ),
    path('api/change-password/', PensionUserChangePassword.as_view(), name='change-password'),

]
