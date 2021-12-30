from django.core.mail import send_mail
from django.conf import settings
from twilio.rest import Client


def otp_by_email(email_id, otp):
    try:
        send_mail(
            subject = 'verification mail',
            message = 'Your Account verification OTP sended sucessfully. Use OTP to verify the account:'+ otp,
            from_email = settings.EMAIL_HOST_USER,
            recipient_list=[email_id, ],
            fail_silently=True,
                )   
        return True
    except:
        return False


def otp_by_sms(phone_number, otp):
    # account_sid = 'AC8e085108eedb178756e301aa355e3798'
    # auth_token = '017b7cb6613a394b488bc0d0bbee7f12'
    account = settings.TWILIO_ACCOUNT_SID
    token = settings.TWILIO_AUTH_TOKEN
    client = Client(account, token)
    message = client.messages.create(
    body = f'Your Account verification OTP sended sucessfully. Use OTP to verify the account.'+otp,
    from_ = f'+17194650389',
    to = phone_number
    )