from rest_framework import serializers
from rest_framework import status
from . models import UserAccountDetails
import math, random
from .sms import otp_by_sms, otp_by_email, reset_password_by_email
from django.contrib.auth.models import User
from rest_framework.response import Response


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
            # return 'Entered OTP is invalid!!Please enter the correct OTP.'
        

# Serializer for Login
class UserLoginSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=255, min_length=2)
    password = serializers.CharField(max_length=65, min_length=8, write_only=True)

    class Meta:
        model = UserAccountDetails
        #fields = ('id', 'email_id', 'password')
        fields = ( 'username', 'password', )

    # validating fields
    # def validate(self, attrs):
    #     email_id = attrs.get('email_id', '')
    #     password = attrs.get('password', '')
    #     print(email_id)
    #     user = UserAccount.objects.get(email_id = email_id)
    #     print(user)


# # Serializer for ForgetPassword
# class UserForgetPasswordSerializer(serializers.Serializer):

#     email_id = serializers.EmailField(max_length = 254)
#     # class Meta:
#     #     model = UserAccount
        

#     def validate_email_id(self, value):
#         # email_id = attrs.get('email_id', '')
#         print(value)
#         try:
#             user = UserAccount.objects.get(email_id = value)
#             print(user)
#             if not user:
#                 raise serializers.ValidationError({'email_id' : ('this email is not registered')})
#             else:
#                 reset_password_by_email(value) 
#         except:
#                 raise serializers.ValidationError({'email_id' : ('this email registered')})

#     def save(self):
#        pass
    
    
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        #print(attrs)
        data = super().validate(attrs)
        #print(data)
        token = self.get_token(self.user)
        #print(token)
        data['user'] = str(self.user)
        data['id'] = self.user.id
        obj = UserAccount.objects.get(username='vishnu')
        data['obj'] = obj.username
        return(data)