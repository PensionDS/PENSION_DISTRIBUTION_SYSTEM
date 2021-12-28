from rest_framework import generics, status
from rest_framework.response import Response
from .serializers import UserRegistrationSerializer


# View for User Registration
class PensionUserRegister(generics.GenericAPIView):
    serializer_class = UserRegistrationSerializer
    def post(self, request, *args, **kwargs):
        serializer = UserRegistrationSerializer(data = request.data)
        serializer.is_valid(raise_exception = True)
        user = serializer.save()
        return Response({
            "user" : serializer.data,
            "message" : "User Created Successfully.  Now perform Login to get your token",
            }, status=status.HTTP_201_CREATED)
