from django.contrib import admin

# Register your models here.

from .models import Profile, Task

admin.site.register(Task) 
admin.site.register(Profile)