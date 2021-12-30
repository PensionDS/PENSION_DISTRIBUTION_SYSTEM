from django.urls import path
from .views import (PensionUserRegister, PensionUserActivation, PensionUserLogin)


urlpatterns = [
    path('user-register/', PensionUserRegister.as_view(), name = 'user-register'),
    path('user-activation/', PensionUserActivation.as_view(), name = 'user-activation'),
    path('user-login/', PensionUserLogin.as_view(), name = 'user-login'),
]
