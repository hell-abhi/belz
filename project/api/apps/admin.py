from django.contrib import admin

# Register your models here.

from .models import User

class UserDetails(admin.ModelAdmin):
    list_display = ("user_id","first_name","last_name","college")

admin.site.register(User, UserDetails)