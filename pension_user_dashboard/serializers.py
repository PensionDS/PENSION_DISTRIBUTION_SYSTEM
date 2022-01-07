from rest_framework import serializers
from .models import UserProfile, BookVerification


class UserProfileSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = UserProfile
        # exclude = ('user',)
        fields = ('DOB', 'Address', 'LGA', 'Name_of_Next_of_Kln', 'Next_of_Kln_email_address',
        'Next_of_Kln_phone', 'Next_of_Kln_address')
        