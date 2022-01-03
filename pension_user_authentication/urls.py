from django.urls import path
from .views import (Home, PensionUserRegister, PensionUserActivation, PensionUserLogin,
Home)


urlpatterns = [
    path('user-register/', PensionUserRegister.as_view(), name = 'user-register'),
    path('user-activation/', PensionUserActivation.as_view(), name = 'user-activation'),
    path('user-login/', PensionUserLogin.as_view(), name = 'user-login'),
   
    path('home/', Home.as_view() ),

]
