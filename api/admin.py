from django.contrib import admin

# Register your models here.

from .models import Profile, Task
from .models import Profile
admin.site.register(Task) 
admin.site.register(Profile)
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User



# Define an inline admin descriptor for Employee model
# which acts a bit like a singleton
class ProfileInLine(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'profile'

# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = (ProfileInLine,)

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)