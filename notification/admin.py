from django.contrib import admin
from notification.models import *
admin.site.register(UserNotification)
admin.site.register(Notification)