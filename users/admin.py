from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(EmailContact)
admin.site.register(ContactNumber)
admin.site.register(UserProfile)
admin.site.register(Interests)