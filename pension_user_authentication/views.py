from rest_framework import generics, status
from rest_framework.response import Response
from django.core.mail import send_mail
from .models import UserAccount
from .serializers import ( UserRegistrationSerializer, AccountActivationSerializer,
 UserLoginSerializer
)

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

    # def post(self, request, *args, **kwargs):
    #     serializer = UserLoginSerializer(data = request.data)
    #     print(request.data)
       
    #     serializer.is_valid()
    #     print(serializer.data)
    #     return Response({
    #         "token" : 'token'
    #     })

    def post(self, request):
        data = request.data
        email_id = data.get('email_id',' ')
        password = data.get('password',' ')

        try:
            user = UserAccount.objects.get(email_id = email_id, password = password)

            if user:
                # auth_token = jwt.encode({'email_id':user.email_id},'JWTSECRETKEYJWTSECRETKEYJWTSECRETKEY')

                serializer = UserLoginSerializer(user)

                data={
                'user': serializer.data,
                # 'token': auth_token
                }

                return Response(data,status=status.HTTP_200_OK)
        except:
            return Response({'details':'Invalid credentials'},status=status.HTTP_401_UNAUTHORIZED)
