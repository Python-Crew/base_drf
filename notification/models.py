from django.db import models
from django.contrib.auth.models import User
class UserNotification(models.Model):
    user = models.OneToOneField(to=User,on_delete=models.CASCADE)

class Notification(models.Model):
    user_notification = models.ForeignKey(to=UserNotification,on_delete=models.CASCADE)
    TYPE_SMS = 'sms'
    TYPE_EMAIL = 'email'
    TYPE_IN_APP = 'In app'

    TYPES = (
        (TYPE_SMS, 'sms'),
        (TYPE_EMAIL, 'email'),
        (TYPE_IN_APP, 'In app'),
    )

    notif_type = models.CharField(max_length=10,choices=TYPES)