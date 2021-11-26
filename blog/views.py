from rest_framework.viewsets import ModelViewSet

from .serializers import (
    PostCommentSerializer,
    PostModelSerializer,
    BlogCategorySerializer,
)
from .models import BlogCategory, Post, PostComment
from .filters import PostFilter, PostCommentFilter

from ckeditor_uploader.views import ImageUploadView
from BaseDRF import settings
import json
import re
import os
from PIL import Image


class BlogCategoryViewSet(ModelViewSet):
    serializer_class = BlogCategorySerializer
    queryset = Post.objects.select_related("parent").all()


class PostModelViewSet(ModelViewSet):
    serializer_class = PostModelSerializer
    queryset = (
        Post.objects.filter(is_published=True)
        .select_related("author", "category")
        .all()
    )
    filterset_class = PostFilter


class PostComment(ModelViewSet):
    serializer_class = PostCommentSerializer
    queryset = (
        PostComment.objects.filter(is_published=True)
        .select_related("author", "post", "parent")
        .all()
    )
    filterset_class = PostCommentFilter


class MyImageUploadView(ImageUploadView):
    def post(self, request, **kwargs):
        base_process = super(MyImageUploadView, self).post(request, **kwargs)

        base_image = json.loads(base_process.content)
        file_name_path = re.findall(r"^[^\.]*", base_image["url"])[0]

        image = Image.open(str(settings.BASE_DIR) + base_image["url"])
        image = image.convert("RGB")
        image.save(str(settings.BASE_DIR) + file_name_path + ".webp", "webp")

        os.remove(str(settings.BASE_DIR) + base_image["url"])

        new_image_url = file_name_path + ".webp"
        base_image["url"] = new_image_url
        base_image["fileName"] = (
            re.findall(r".+(\/.+)$", file_name_path)[0][1:] + ".webp"
        )
        changed_json = json.dumps(base_image).encode("ascii")
        base_process.content = changed_json
        return base_process
