from rest_framework.viewsets import ModelViewSet

from . import serializers
from . import models

from ckeditor_uploader.views import ImageUploadView


class BlogCategoryViewSet(ModelViewSet):
    serializer_class = serializers.PostModelSerializer
    queryset = models.Post.objects.all()


class PostModelViewSet(ModelViewSet):
    serializer_class = serializers.PostModelSerializer
    queryset = models.Post.objects.filter(is_published=True)

    def get_queryset(self):
        qs = self.queryset
        category_param = self.request.query_params.get("category")
        try:
            if category_param:
                return qs.filter(category_id=category_param)
        except:
            return super().get_queryset()


class PostComment(ModelViewSet):
    serializer_class = serializers.PostCommentSerializer
    queryset = models.PostComment.objects.filter(is_published=True)


class MyImageUploadView(ImageUploadView):
    def post(self, request, **kwargs):
        return super(MyImageUploadView, self).post(request, **kwargs)
