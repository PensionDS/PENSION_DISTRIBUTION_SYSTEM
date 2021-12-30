from django.core.mail import send_mail
from django.conf import settings
# from twilio.rest import Client
def otp_by_email(email_id, otp):
    try:
        send_mail(
            subject = 'verification mail',
            message = 'Your Account verification OTP sended sucessfully. Use OTP to verify the account:'+ otp,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[email_id, ],
            fail_silently=True,
                )   
        return True
    except:
        return False


# def otp_by_sms(otp):
#     # account_sid = settings.account_sid
#     # auth_token = settings.auth_token
#     account_sid='AC8e085108eedb178756e301aa355e3798'
#     auth_token='62402772197f7a5cbe172538ee45d10d'

#     client = Client(account_sid, auth_token)
#     message = client.messages.create(
#     body = f'Your Account verification OTP sended sucessfully. Use OTP to verify the account.'+otp,
#     from_ = f'+17194650389',
#     # to = phone_number
#     to=f'+918590017269'
#     )