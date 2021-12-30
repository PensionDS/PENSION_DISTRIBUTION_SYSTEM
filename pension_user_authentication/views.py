from rest_framework import generics, status
from rest_framework.response import Response
from django.core.mail import send_mail

from .serializers import UserRegistrationSerializer, AccountActivationSerializer


# View for User Registration
class PensionUserRegister(generics.GenericAPIView):
    serializer_class = UserRegistrationSerializer

    def post(self, request, *args, **kwargs):
        serializer = UserRegistrationSerializer(data = request.data)
        serializer.is_valid(raise_exception = True)
        user = serializer.save()
        return Response({
            "user" : serializer.data,
            "message" : "To verify your account please enter the OTP.",
            }, status = status.HTTP_201_CREATED)


# View for Account Activation
class PensionUserActivation(generics.GenericAPIView):
    serializer_class = AccountActivationSerializer

    def post(self, request, *args, **kwargs):
        serializer = AccountActivationSerializer(data = request.data)
        serializer.is_valid(raise_exception = True)
        user = serializer.save()
        return Response({
            "user" : serializer.data,
            "message" : "Your account activated successfully by OTP, Please Login!!",
            }, status = status.HTTP_201_CREATED)
