from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import UserProfile, BookVerification
from .serializers import ( UserProfileSerializer
)

# View for UserProfile
class PensionUserProfile(generics.GenericAPIView):
    serializer_class = UserProfileSerializer

    def post(self, request):
        serializer = UserProfileSerializer(data = request.data)
        data = {}
        if serializer.is_valid():
            user = UserProfile.objects.create(
            user = request.user,
            DOB = serializer.validated_data['DOB'],
            Address = serializer.validated_data['Address'],
            LGA = serializer.validated_data['LGA'], 
            Name_of_Next_of_Kln = serializer.validated_data['Name_of_Next_of_Kln'],
            Next_of_Kln_email_address = serializer.validated_data['Next_of_Kln_email_address'],
            Next_of_Kln_phone = serializer.validated_data['Next_of_Kln_phone'],
            Next_of_Kln_address = serializer.validated_data['Next_of_Kln_address'],
            )
            user.save()
            data['response'] = 'fields added sucessfuly'
        else:
            data = serializer.errors
        return Response(data)

    def put(self, request):
        user = UserProfile.objects.get(user = request.user)
        data = {}
        serializer = UserProfileSerializer(user, data = request.data, partial = True)
        if serializer.is_valid():
            serializer.save()
            data['response'] = 'profile updated sucessfully'
            # return Response(serializer.data) 
            return Response(data)   
        else:
            data = serializer.errors
        return Response(data)
        