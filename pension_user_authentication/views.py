from rest_framework import generics, status
from rest_framework.response import Response
from django.conf import settings
import jwt
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.views import APIView

from .models import UserAccount
from .serializers import ( UserRegistrationSerializer, AccountActivationSerializer,
 UserLoginSerializer
)
from .utils import generate_access_token, generate_refresh_token, get_tokens_for_user


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


# View for User Login
class PensionUserLogin(generics.GenericAPIView):
    serializer_class = UserLoginSerializer

# 1.....
    # def post(self, request):
    #     data = request.data
    #     email_id = data.get('email_id',' ')
    #     password = data.get('password',' ')

    #     try:
    #         user = UserAccount.objects.get(email_id = email_id, password = password)
    #         print(user.is_active)
    #         if user:
    #             if user.is_active:
    #                 auth_token = jwt.encode({'email_id':user.email_id, 'password':user.password}, settings.JWT_SECRET_KEY)
    #                 #auth_token = jwt.encode({'username':user.username, 'password':user.password}, settings.JWT_SECRET_KEY)
    #                 serializer = UserLoginSerializer(user)

    #                 data={
    #                 'user': serializer.data,
    #                 'token': auth_token
    #                 }

    #                 return Response(data,status=status.HTTP_200_OK)
    #             else:
    #                 return Response({'details':'Account is not activated yet, Please enter the OTP to activate your account'},status=status.HTTP_401_UNAUTHORIZED)
    #     except:
    #         return Response({'details':'Invalid credentials'},status=status.HTTP_401_UNAUTHORIZED)

# 2.....
    def post(self, request):
        data = request.data
        email_id = data.get('email_id',' ')
        password = data.get('password',' ')

        try:
            user = UserAccount.objects.get(email_id = email_id, password = password)
            if user:
                if user.is_active:
                    serializer = UserLoginSerializer(user)
                   
                    #token = get_tokens_for_user(user)
                    
                    access_token = generate_access_token(user)
                    refresh_token = generate_refresh_token(user)
                                   

                    data={
                    'user': serializer.data,
                    'access_token': access_token,
                    'refresh_token': refresh_token
                    #'token': token
                    }

                    return Response(data,status=status.HTTP_200_OK)
                else:
                    return Response({'details':'Account is not activated yet, Please enter the OTP to activate your account'},status=status.HTTP_401_UNAUTHORIZED)
        except:
            return Response({'details':'Invalid credentials'},status=status.HTTP_401_UNAUTHORIZED)

<<<<<<< HEAD
=======


class Home(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)
>>>>>>> 2effea55f57343470fa8f3157a4c466647418721
