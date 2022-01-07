from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.views import APIView
from .models import UserAccountDetails
from .serializers import ( UserRegistrationSerializer, AccountActivationSerializer,
    TokenGenerationSerializer, TokenGenerationSerializer, ChangePasswordSerializer,
    ResendOTPSerializer
    )


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


# View for ResendOTP
class PensionResendOTP(generics.GenericAPIView):
    serializer_class = ResendOTPSerializer

    def post(self, request):
        serializer = ResendOTPSerializer(data=request.data)
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
    

# View for Change Password
class PensionUserChangePassword(generics.UpdateAPIView):
    serializer_class = ChangePasswordSerializer
    model = User
    permission_classes = (IsAuthenticated,)

    def get_object(self, queryset=None):
        obj = self.request.user
        return obj

    def update(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            # Check old password
            if not self.object.check_password(serializer.data.get("old_password")):
                return Response({"old_password": ["Wrong password."]})
            # set_password also hashes the password that the user will get
            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            response = {
                'status': 'success',
                'message': 'Password updated successfully',
                'data': []
            }
            return Response(response)
        return Response(serializer.errors)
