from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import UserProfile, BookVerification, UserServiceStatus, UserAccountDetails
from .models import UserProfile, BookVerification, UserServiceStatus
from pension_user_authentication.models import UserAccountDetails
from .serializers import ( UserProfileSerializer, UserBookVerificationSerializer,
    UserServiceStatusSerializer
)


# View for User Home
class PensionUserHome(generics.GenericAPIView):
    permission_classes = (IsAuthenticated,)
    
    def get_queryset(self):
        user = self.request.user
        user1 = UserProfile.objects.filter(user = user)
        print(user1)
        return UserProfile.objects.filter(user = user)

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


# View  for User Profile Completion and Update and Display.
class PensionUserProfile(generics.GenericAPIView):
    serializer_class = UserProfileSerializer
    permission_class = (IsAuthenticated,)

    def get(self, request):       
        user = UserProfile.objects.get(user = request.user)
        username = User.objects.get(username = request.user)
        phone_number = UserAccountDetails.objects.get(user = request.user)
        service_status = UserServiceStatus.objects.get(user = request.user)

        data={}
        account_data = {}

        data['username'] = username.username
        data['email'] = username.email
        data['phone_number'] = phone_number.phone_number
        data['DOB'] = user.DOB
        data['Address'] = user.Address
        data['LGA'] = user.LGA
        data['Name_of_Next_of_Kln'] = user.Name_of_Next_of_Kln
        data['Next_of_Kln_email_address'] = user.Next_of_Kln_email_address
        data['Next_of_Kln_phone'] = user.Next_of_Kln_phone
        data['Next_of_Kln_address'] = user.Next_of_Kln_address

        account_data['service_status'] = service_status.service_status

        return Response({"Basic Information " : data, "Account Information" : account_data })

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
            return Response(data)   
        else:
            data = serializer.errors
        return Response(data)

    def get(self, request):
        user = UserProfile.objects.get(user = request.user)
        username = User.objects.get(username = request.user)
        phone_number = UserAccountDetails.objects.get(user = request.user)
        service_status = UserServiceStatus.objects.get(user = request.user)
        data={}
        data['service_status'] = service_status.service_status
        data['username'] = username.username
        data['email'] = username.email
        data['phone_number'] = phone_number.phone_number
        data['DOB'] = user.DOB
        data['Address'] = user.Address
        data['LGA'] = user.LGA
        data['Name_of_Next_of_Kln'] = user.Name_of_Next_of_Kln
        data['Next_of_Kln_email_address'] = user.Next_of_Kln_email_address
        data['Next_of_Kln_phone'] = user.Next_of_Kln_phone
        data['Next_of_Kln_address'] = user.Next_of_Kln_address
        return Response({'Profile Details' : data})


# View for Book verification
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
            data['response'] = 'Book verification sucessfully done!'
        else:
            data = serializer.errors
        return Response(data)
