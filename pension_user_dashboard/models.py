from django.db import models
from django.contrib.auth.models import User
from pension_user_authentication.models import UserAccountDetails


# Model for UserProfile
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    DOB = models.DateField(max_length = 8, null = False, blank = False)
    Address = models.TextField(null = False, blank = False)
    LGA = models.CharField(max_length = 50, null = False, blank = False)
    Name_of_Next_of_Kln = models.CharField(max_length = 50, null = False, blank = False)
    Next_of_Kln_email_address = models.EmailField(max_length = 254, null = False, blank = False)
    Next_of_Kln_phone = models.CharField(max_length = 13, null = False, blank = False)
    Next_of_Kln_address = models.CharField(max_length = 50, null = False, blank = False)

    def __str__(self):
        return self.user.username

