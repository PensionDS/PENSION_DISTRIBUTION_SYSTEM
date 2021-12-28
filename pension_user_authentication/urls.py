from django.urls import path
from .views import PensionUserRegister


urlpatterns = [
    path('user-register/', PensionUserRegister.as_view(), name = 'user-register'),
]
