from django.contrib import admin

# Register your models here.
from .models import Building, Spaces, Device, NFC

admin.site.register([Building, Spaces, Device, NFC ])