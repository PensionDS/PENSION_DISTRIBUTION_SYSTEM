from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import ( UserRegistrationSerializer, AccountActivationSerializer,
TokenGenerationSerializer)



# View for User Registration
class PensionUserRegister(generics.GenericAPIView):
    serializer_class = UserRegistrationSerializer

    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            user = serializer.save()
            data['response'] = "An otp has sent to the phone number  and verify  your account "
        else:
            data = serializer.errors
        return Response(data)


# View for Account Activation
class PensionUserActivation(generics.GenericAPIView):
    serializer_class = AccountActivationSerializer

    def post(self, request, *args, **kwargs):
        serializer = AccountActivationSerializer(data = request.data)
        data = {}
        if serializer.is_valid():
            user = serializer.save()
            data['response'] = "Your account activated successfully by OTP, Please Login!!"
        else:
            data = serializer.errors
        return Response(data)
       
# View for Token generation
class TokenGenerationView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = TokenGenerationSerializer

      
class Home(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)
    
