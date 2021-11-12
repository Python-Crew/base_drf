from django.db import models
from rest_framework import fields,serializers


class NotificationInputsSerializer(serializers.Serializer):
    TYPE_SMS = 'sms'
    TYPE_EMAIL = 'email'
    TYPE_IN_APP = 'In app'

    TYPES = (
        (TYPE_SMS, 'sms'),
        (TYPE_EMAIL, 'email'),
        (TYPE_IN_APP, 'In app'),
    )
    notif_type = fields.ChoiceField(choices=TYPES)