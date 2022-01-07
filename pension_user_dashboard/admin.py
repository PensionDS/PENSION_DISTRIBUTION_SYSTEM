from django.contrib import admin
from .models import UserProfile, BookVerification


# Register : User Profile Model
admin.site.register(UserProfile)

admin.site.register(BookVerification)
