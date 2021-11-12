from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from notification.models import UserNotification


@receiver(post_save, sender=User)
def auto_create_user_notification(sender, instance, created, **kwargs):
    if created:
        UserNotification.objects.create(user=instance)