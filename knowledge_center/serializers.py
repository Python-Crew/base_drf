from .models import *
from rest_framework import serializers
from rest_framework_recursive.fields import RecursiveField


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="category_detail")
    children = RecursiveField(
        many=True,
        read_only=True,
    )

    class Meta:
        model = Category
        fields = ["url", "id", "title", "children", "main_page_category"]
