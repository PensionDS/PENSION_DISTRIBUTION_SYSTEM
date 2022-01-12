from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView
from .serializers import NotificationSendSerializer
from django.contrib.auth.models import User
from .models import UserNotification
from rest_framework.response import Response
from rest_framework import status
from channels.layers import get_channel_layer
from rest_framework.permissions import IsAuthenticated
from asgiref.sync import async_to_sync
# Create your views here.
class PensionUserNotificationSend(APIView):
    serializer_class = NotificationSendSerializer

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            serializer = self.serializer_class(data=request.data)
            if serializer.is_valid():
                serializer.save()
                user= serializer.data['user']
                username = User.objects.get(id=user).username
                channel_layer = get_channel_layer()
                notification = serializer.data['notification']
                notification_objs = UserNotification.objects.filter(is_seen=False, user= user).count()
                data = {'count':notification_objs,'current_notifications':notification}
                async_to_sync(channel_layer.send)(
                    username,{
                        'type':'send_notification',
                        'value':data
                    }
                )
        except:
            data= serializer.errors
        return Response(data, status=status.HTTP_201_CREATED)



class PensionNotificationReceive(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request):
        
        username = request.user.username
        channel_layer = get_channel_layer()
        try:
            notification = async_to_sync(channel_layer.receive)(username)
            print(notification)
        except Exception as e:
            print(e)
        return Response(notification)


class Testview(CreateAPIView):
    serializer_class = NotificationSendSerializer
    queryset = UserNotification.objects.all()
