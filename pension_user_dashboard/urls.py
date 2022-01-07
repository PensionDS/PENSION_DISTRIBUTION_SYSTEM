from django.urls import path
from . views import(
    PensionUserProfile
)
urlpatterns = [
    path('user-profile/', PensionUserProfile.as_view(), name = 'user-profile'),   
]
