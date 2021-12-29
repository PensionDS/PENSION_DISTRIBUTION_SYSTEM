from rest_framework import generics, status
from rest_framework.response import Response
from django.core.mail import send_mail
from django.conf import settings
from .serializers import UserRegistrationSerializer

from twilio.rest import Client



# # Function to generate OTP
# def generateOTP() :
#     # Declare a digits variable 
#     # which stores all digits
#     digits = "0123456789"
#     OTP = ""
 
#     for i in range(5) :
#         OTP += digits[math.floor(random.random() * 10)]
 
#     return OTP
# Calling function to generate OTP

# Function to check email is verified or not
# def otp_by_email(email_id, otp):
#     try:
#         send_mail(
#             subject = 'verification mail',
#             message = 'Your Account verification OTP sended sucessfully. Use OTP to verify the account:'+ otp,
#             from_email=settings.EMAIL_HOST_USER,
#             recipient_list=[email_id, ],
#             fail_silently=True,
#                 )   
#         return True
#     except:
#         return False


# def otp_by_sms(phone_number, otp):
#     account_sid = 'AC8e085108eedb178756e301aa355e3798'
#     auth_token = '62402772197f7a5cbe172538ee45d10d'
#     client = Client(account_sid, auth_token)
#     message = client.messages.create(
#     body = f'Your Account verification OTP sended sucessfully. Use OTP to verify the account.'+otp,
#     from_ = f'+17194650389',
#     to = phone_number
#     )
    

# View for User Registration
class PensionUserRegister(generics.GenericAPIView):
    serializer_class = UserRegistrationSerializer

    def post(self, request, *args, **kwargs):
        serializer = UserRegistrationSerializer(data = request.data)
        serializer.is_valid(raise_exception = True)

        

        # Calling function to send otp using  email
        # otp_by_email(request.data['email_id'], otp)

        # Calling function to send otp using sms
        # otp_by_sms(request.data['phone_number'], otp)
        user = serializer.save()
        print(user)
        return Response({
            "user" : serializer.data,
            "message" : "To verify your account please enter the OTP.",
            }, status=status.HTTP_201_CREATED)

