from rest_framework import serializers
from . models import UserAccount


# serializer for User Registration
class UserRegistrationSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserAccount
        fields = ('id','username','email_id','phone_number', 'password', 'confirm_password')
        extra_kwargs = {
            'password':{'write_only': True},
        }
    def create(self, validated_data):
        user = UserAccount.objects.create(username = validated_data['username'], 
        email_id = validated_data['email_id'],
        phone_number = validated_data['phone_number'],password = validated_data['password'],
        confirm_password = validated_data['confirm_password'])
        return user
