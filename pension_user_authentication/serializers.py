from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
import math, random
from .sms import otp_by_sms, otp_by_email
from django.contrib.auth.models import User
from . models import UserAccountDetails


# Serializer for User Registration
class UserRegistrationSerializer(serializers.ModelSerializer):
    phone_number = serializers.IntegerField(write_only = True)
    confirm_password = serializers.CharField(write_only = True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'confirm_password', 'phone_number' )
        extra_kwargs = {
            'password' : {'write_only' : True},
            'confirm_password' : {'write_only' : True}
        }
       
    # validating all fields
    def validate(self, attrs):
        username = attrs.get('username', '')
        phone_number = attrs.get('phone_number', '')
        password = attrs.get('password', '')
        confirm_password = attrs.get('confirm_password', '')
        
        # if len(str(phone_number)) != 13:
        #     raise serializers.ValidationError({'phone_number' : ('phone_number  is not valid')})
        
        if password != confirm_password:
            raise serializers.ValidationError({'password' : ('password mismatch, please enter same password')})
        return super().validate(attrs)

    def create(self, validated_data):        
        # Function to generate OTP
        def generateOTP() :
            digits = "123456789"
            OTP = ""
 
            for i in range(5) :
                OTP += digits[math.floor(random.random() * 9)]
                
            return OTP

        OTP = generateOTP()

        # Calling function to send otp using  email
        otp_by_email(validated_data['email'], OTP)

        # Calling function to send otp using sms
        # otp_by_sms(validated_data['phone_number'], OTP)

        user = User.objects.create(
           username = validated_data['username'],
           email =validated_data['email'],
            )
            
        userreg = UserAccountDetails.objects.create(
            user = user,
            phone_number = validated_data['phone_number'],
            otp = OTP,
            )

        user.set_password(validated_data['password'])

        #otp_by_email(validated_data['email_id'], OTP)

        # Calling function to send otp using sms
        #otp_by_sms(validated_data['phone_number'], OTP)

        user.save()
        userreg.save()
        
        return user


# Serializer for Account Activation
class AccountActivationSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAccountDetails
        fields = ('otp',)

    def create(self, validated_data):
        try:
            user =UserAccountDetails.objects.get(otp = validated_data['otp'])
        
            if user:
                user.is_active=True
                user.save()
                return user
        except:
            raise serializers.ValidationError({'message' : ('Entered OTP is invalid!!Please enter the correct OTP.')})
        

# Serializer for Token generation by extending TokenObtainPairSerializer
class TokenGenerationSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super(TokenGenerationSerializer, cls).get_token(user)

        return token

