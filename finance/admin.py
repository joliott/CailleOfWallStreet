from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from finance.models import Operations, User

# Register your models here.
admin.site.register(Operations)
admin.site.register(User, UserAdmin)