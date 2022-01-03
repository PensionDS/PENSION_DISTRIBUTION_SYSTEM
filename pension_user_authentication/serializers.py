from rest_framework import serializers
from rest_framework import status
from . models import UserAccount
import math, random
from .sms import otp_by_sms, otp_by_email


# Serializer for User Registration
class UserRegistrationSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserAccount
        fields = ('id', 'username', 'email_id', 'phone_number', 'password', 'confirm_password')
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

        if len(username) >= 4:
            for char in username:
                if  not (("A" <= char and char <= "Z") or ("a" <= char and char <= "z") or (char == " ")):
                    raise serializers.ValidationError({'username' : ('username should not  contain numbers, white space and special characters')})              
        else:
            raise serializers.ValidationError({'username' : ('username should contains atleast 4 characters')})
        
        if len(phone_number) != 13:
            raise serializers.ValidationError({'phone_number' : ('phone_number  is not valid')})
        
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

        OTP=generateOTP()
        # Calling function to send otp using  email
        otp_by_email(validated_data['email_id'], OTP)

        # Calling function to send otp using sms
        otp_by_sms(validated_data['phone_number'], OTP)

        user = UserAccount.objects.create(**validated_data)
        user.otp=OTP
        user.save()
        
        return user


# Serializer for Account Activation
class AccountActivationSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserAccount
        fields = ('id', 'otp')

    def create(self, validated_data):
        try:
            user = UserAccount.objects.get(otp = validated_data['otp'])
        
            if user:
                user.is_active=True
                user.save()
                return user
        except:
            raise serializers.ValidationError({'message' : ('Entered OTP is invalid!!Please enter the correct OTP.')})
            # return 'Entered OTP is invalid!!Please enter the correct OTP.'
        

# Serializer for Login
class UserLoginSerializer(serializers.ModelSerializer):
    # email_id = serializers.EmailField(max_length=255, min_length=2)
    # password = serializers.CharField(max_length=65, min_length=8, write_only=True)

    class Meta:
        model = UserAccount
        #fields = ('id', 'email_id', 'password')
        fields = ('id', 'email_id', 'password', 'username')

    # validating fields
    # def validate(self, attrs):
    #     email_id = attrs.get('email_id', '')
    #     password = attrs.get('password', '')
    #     print(email_id)
    #     user = UserAccount.objects.get(email_id = email_id)
    #     print(user)
