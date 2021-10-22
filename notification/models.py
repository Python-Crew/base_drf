from django.db import models
from django.contrib.auth.models import User
class UserNotification(models.Model):
    user = models.OneToOneField(to=User,on_delete=models.DO_NOTHING)

class Notification(models.Model):
    user_notification = models.ForeignKey(to=UserNotification,on_delete=models.DO_NOTHING)
    TYPE = (
    (0, "Email"),
    (2, "In app"),
    (1, "SMS")
    )

    notif_type = models.CharField(max_length=10,choices=TYPE)