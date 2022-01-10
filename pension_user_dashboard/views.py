from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import UserProfile, BookVerification, UserServiceStatus
from .serializers import ( UserProfileSerializer, UserBookVerificationSerializer,
    UserServiceStatusSerializer
)


# View for User Home
class PensionUserHome(generics.GenericAPIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request):
        data = {}
        user = request.user
        data['user'] = user.username
        return Response(data)
        

# View for User service status 
class PensionUserStatus(generics.GenericAPIView):
    serializer_class = UserServiceStatusSerializer
    permission_classes = (IsAuthenticated,)
    def post(self, request):
        serializer = UserServiceStatusSerializer(data = request.data)
        data = {}
        if serializer.is_valid():
            user = UserServiceStatus.objects.create(
                user = request.user,
                service_status = serializer.validated_data['service_status'],
            )
            user.save()
            data['response'] = 'Service status added'
        else:
            data = serializer.errors
        return Response(data)


# View  for User Profile Completion and Update.
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
        

class PensionUserBookVerification(generics.GenericAPIView):
    serializer_class = UserBookVerificationSerializer
    permission_classes = (IsAuthenticated,)
    def post(self, request):
        serializer = UserBookVerificationSerializer(data = request.data)
        data = {}
        if serializer.is_valid():
            user = BookVerification.objects.create(
                user = request.user,
                Date = serializer.validated_data['Date'],
            )
            user.save()
            # serializer.save()
            data['response'] = 'Book verification sucessfully done!'
        else:
            data = seralizer.errors
        return Response(data)
