
from rest_framework.viewsets import ModelViewSet


from . import serializers
from . import models


class PostModelViewSet(ModelViewSet):
    serializer_class = serializers.PostModelSerializer
    queryset = models.Post.objects.all()
