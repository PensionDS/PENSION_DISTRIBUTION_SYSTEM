from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import ( UserRegistrationSerializer, AccountActivationSerializer,
TokenGenerationSerializer, UserForgetPasswordSerializer, UserChangePasswordSerializer)
from .models import UserAccountDetails
from django.contrib.auth.models import User

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
            user =UserAccountDetails.objects.get(otp = request.data['otp'])
           
            user_obj =User.objects.get(username = user.user)
        
            user_obj.is_active = True
            user_obj.save()
            data['response'] = "Your account activated successfully by OTP, Please Login!!"
        else:
            data = serializer.errors
        return Response(data)


# View for Token generation
class TokenGenerationView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = TokenGenerationSerializer


# Home view      
class Home(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)
    

# View for forget password
class PensionUserForgetPassword(generics.GenericAPIView):
    serializer_class = UserForgetPasswordSerializer
    
    def post(self, request, *args, **kwargs):
        serializer = UserForgetPasswordSerializer(data = request.data)
        data = {}
        if serializer.is_valid(raise_exception = True):
            serializer.save()
            data['response'] = "To change your password, the link for reset paasword is send to yor email account"
        else:
            data = serializer.errors
        return Response(data)


class PensionChangePassword(generics.GenericAPIView):
    serializer_class = UserChangePasswordSerializer

    def post(self, request, *args, **kwargs):
        serializer = UserChangePasswordSerializer(data = request.data)
        data = {}
        if serializer.is_valid(raise_exception = True):
            serializer.save()
            data['response'] = "Password changed successfully, please login with new password"
        else:
            data = serializer.errors
        return Response(data)
        