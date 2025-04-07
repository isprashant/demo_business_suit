from django.contrib import admin

# Register your models here.
from .models import Building, Space, Device, NFC

admin.site.register([Building, Space, Device, NFC ])