from django.contrib.auth.admin import UserAdmin
from django.contrib import admin

from .models import Account


# Register your models here.
admin.site.register(Account, UserAdmin)
