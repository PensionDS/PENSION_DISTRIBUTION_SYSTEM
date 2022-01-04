import datetime
import jwt
from django.conf import settings


def generate_access_token(user):
    access_token_payload = {
        #'user_id': user.id,
        'username' : user.username,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(days=0, minutes=10),
        'iat': datetime.datetime.utcnow(),
    }
    access_token = jwt.encode(access_token_payload,
                               settings.SECRET_KEY, algorithm='HS256').decode('utf-8')
    #access_token = jwt.encode(access_token_payload,
    #                           settings.SECRET_KEY, algorithm='HS256').decode('utf-8')
    return access_token


def generate_refresh_token(user):
    refresh_token_payload = {
        #'user_id': user.id,
        'username' : user.username,
        #'password' : user.password,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(days=7),
        'iat': datetime.datetime.utcnow()
    }
   
    refresh_token = jwt.encode(
         refresh_token_payload, settings.REFRESH_TOKEN_SECRET, algorithm='HS256').decode('utf-8')

    #refresh_token = jwt.encode(
    #     refresh_token_payload, 'key', algorithm='HS256').decode('utf-8')
    return refresh_token




from rest_framework_simplejwt.tokens import RefreshToken

def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }

