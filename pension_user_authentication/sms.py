from django.core.mail import send_mail
from django.conf import settings
from twilio.rest import Client
from django.contrib.auth.models import User


# Function to send OTP through email
def otp_by_email(email, otp):
    try:
        send_mail(
            subject = 'verification mail',
            message = 'Your Account verification OTP sended sucessfully. Use OTP to verify the account:'+ otp,
            from_email = settings.EMAIL_HOST_USER,
            recipient_list=[email, ],
            fail_silently=True,
                )   
        return True
    except:
        return False


# Function to send OTP through sms
def otp_by_sms(phone_number, otp):
    account = settings.TWILIO_ACCOUNT_SID
    token = settings.TWILIO_AUTH_TOKEN
    client = Client(account, token)
    message = client.messages.create(
    body = f'Your Account verification OTP sended sucessfully. Use OTP to verify the account.'+otp,
    from_ = settings.TWILIO_FROM_,
    to = phone_number
    )


# Function to send link to change password
def reset_password_by_email(email_id):
    try:
        send_mail(
            subject = 'Reset Password Link',
            message = 'To reset password to click the link and '+ 'http://127.0.0.1:8000/pension_user_authentication/change-password/' ,
            from_email = settings.EMAIL_HOST_USER,
            recipient_list=[email_id, ],
            fail_silently=True,
                )   
        return True
    except:
        return False