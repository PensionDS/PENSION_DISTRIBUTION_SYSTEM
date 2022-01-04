from django.urls import path
from .views import (PensionUserRegister,PensionUserActivation,customjwt #PensionUserLogin,
# Home, PensionUserForgetPassword, PensionChangePassword, #UserRegistration
)


urlpatterns = [
    path('user-register/', PensionUserRegister.as_view(), name = 'user-register'),
    path('user-activation/', PensionUserActivation.as_view(), name = 'user-activation'),

    # path('user-login/', PensionUserLogin.as_view(), name = 'user-login'),
    # path('forget-password/', PensionUserForgetPassword.as_view(), name = 'forget-password'),
    # path('change-password/', PensionChangePassword.as_view(), name = 'change-password'),
    # # path('use-reg/', UserRegistration.as_view(), name = 'use-reg'),

    path('user-login/', PensionUserLogin.as_view(), name = 'user-login'),
    path('forget-password/', PensionUserForgetPassword.as_view(), name = 'forget-password'),
    path('change-password/', PensionChangePassword.as_view(), name = 'change-password'),
   

    
    # path('home/', Home.as_view() ),
    path('token/', customjwt.as_view(), name='token'),

]
