from django.contrib import admin
from .models import UserProfile, BookVerification,UserServiceStatus


# Register : User Profile Model
admin.site.register(UserProfile)

# Register : Book verification model
admin.site.register(BookVerification)

#Register :User service status model
admin.site.register(UserServiceStatus)
