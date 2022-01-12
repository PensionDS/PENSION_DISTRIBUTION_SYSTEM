from rest_framework import serializers
from .models import UserNotification


class NotificationSendSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserNotification
        fields = ('user', 'notification',)
