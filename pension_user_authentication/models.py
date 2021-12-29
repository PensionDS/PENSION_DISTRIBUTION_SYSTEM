from django.db import models


#Model for User Registration 
class UserAccount(models.Model):
    username = models.CharField(max_length = 50, null = False, blank = False)
    email_id = models.EmailField(max_length = 251, null = False, blank = False, unique = True)
    phone_number = models.CharField(max_length = 13, null = False, blank = False)
    password = models.CharField(max_length = 16, null = False, blank = False)
    confirm_password = models.CharField(max_length = 16, null = False, blank = False)
    otp = models.IntegerField(default = 00000)
    is_active = models.BooleanField(default = False) 
    

    def __str__(self):
        return self.username
