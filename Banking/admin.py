from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import CustomUser, Bank, Sube

admin.site.register(Sube)
admin.site.register(CustomUser)
admin.site.register(Bank)