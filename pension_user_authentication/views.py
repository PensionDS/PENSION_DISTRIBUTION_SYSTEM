from rest_framework import generics, status
from rest_framework.response import Response
from django.core.mail import send_mail

from .serializers import UserRegistrationSerializer


# View for User Registration
class PensionUserRegister(generics.GenericAPIView):
    serializer_class = UserRegistrationSerializer

    def post(self, request, *args, **kwargs):
        serializer = UserRegistrationSerializer(data = request.data)
        serializer.is_valid(raise_exception = True)
        user = serializer.save()
        print(user)
        return Response({
            "user" : serializer.data,
            "message" : "To verify your account please enter the OTP.",
            }, status=status.HTTP_201_CREATED)

