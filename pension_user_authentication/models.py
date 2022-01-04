from django.db import models
from django.contrib.auth.models import User

#Model for User Registration 
class UserAccountDetails(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    phone_number = models.CharField(max_length = 13, null = False, blank = False)
    otp = models.IntegerField(default = 00000)
    is_active = models.BooleanField(default = False) 
    
    def __str__(self):
        return self.user.username