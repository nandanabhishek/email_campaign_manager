from django.contrib import admin

# Register your models here.
from .models import Subscriber, Campaign

admin.site.register(Subscriber)
admin.site.register(Campaign)
