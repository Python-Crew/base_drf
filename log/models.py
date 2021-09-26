import logging

from django.db import models
 # Import ContentType model to use in our class Models
from django.contrib.contenttypes.models import ContentType
# Add Necessary Fields for use in Models
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation

# Create your models here.
class Log(models.Model):
    """
    Log model for using as a GenericForeignKey
    """
    title = models.CharField('Title', max_length=128)
    decription = models.TextField('Description', null=True, blank=True)
    # ? Passing exception error code.
    exception = models.TextField(null=True)
    # Generating ContentType Field
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    # Generic ForeignKey for using in other model
    related_object = GenericForeignKey('content_type', 'object_id')

