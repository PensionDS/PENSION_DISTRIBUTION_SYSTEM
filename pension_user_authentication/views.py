from rest_framework import generics, status
from rest_framework.response import Response
from django.core.mail import send_mail
from django.conf import settings
from .serializers import UserRegistrationSerializer


# Function to check email is verified or not
def email_verification(email):
    to_email_id = email
    print(to_email_id)
    mail_subject = 'verification mail'
    message = 'mail from celery'
    from_email='vishnusajeevks@gmail.com'
    #to_mail = '12vishnuks@gmail.com'
    to_mail = to_email_id
    try:
        send_mail(subject=mail_subject,
                message=message,
                from_email=settings.EMAIL_HOST_USER,
                #from_email = from_email,
                recipient_list=[to_mail,],
                fail_silently=True,
                ) 
        print('mail sent...')
        return True
    except:
        return False



# View for User Registration
class PensionUserRegister(generics.GenericAPIView):
    serializer_class = UserRegistrationSerializer
    def post(self, request, *args, **kwargs):
        serializer = UserRegistrationSerializer(data = request.data)
        serializer.is_valid(raise_exception = True)
    
        # Checking mail id is valid or not by sending email
        if not email_verification(request.data['email_id']):
                return Response({
                "message" : "Entered data is not valid please check the details again",
                }, status=status.HTTP_404_NOT_FOUND)

        user = serializer.save()
        return Response({
            "user" : serializer.data,
            "message" : "User Created Successfully.  Now perform Login to get your token",
            }, status=status.HTTP_201_CREATED)
