from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.
''' Model for User Registration '''
class UserAccount(models.Model):
    username = models.CharField(max_length = 50, null = False, blank = False)
    email_id = models.EmailField(max_length = 251, null = False, blank = False, unique = True)
    phone_number = PhoneNumberField()
    password = models.CharField(max_length = 16, null = False, blank = False)
    confirm_password = models.CharField(max_length = 16, null = False, blank = False)

    def __str__(self):
        return self.username
