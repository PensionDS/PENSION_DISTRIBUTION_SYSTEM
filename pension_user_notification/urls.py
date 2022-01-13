from django.urls import path
from . views import(
    PensionUserNotificationSend, PensionNotificationReceive
    )


urlpatterns = [
    path('notification-send/', PensionUserNotificationSend.as_view(), name = 'notification-send'),
    path('notification-receive/', PensionNotificationReceive.as_view(), name = 'notification-receive'),   
]
