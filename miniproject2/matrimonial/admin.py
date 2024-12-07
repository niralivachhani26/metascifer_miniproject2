from django.contrib import admin
from .models import CustomUser,FriendRequest,ContactMessage

admin.site.register(CustomUser)
admin.site.register(FriendRequest)
admin.site.register(ContactMessage)

# Register your models here.
