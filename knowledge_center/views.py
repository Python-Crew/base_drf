from knowledge_center.serializers import *
from .models import *
from rest_framework.decorators import action
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404
from rest_framework import viewsets

# Create your views here.


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Knowledge_Center_Category.objects.all()
    serializer_class = KnowledgeCenterCategorySerializer

    def retrieve(self, request, pk):
        categories_in_db = get_object_or_404(self.queryset, pk=pk)
        serializer = self.get_serializer(categories_in_db)
        return Response(serializer.data)

    @action(detail=False, methods=["get"])
    def selected(self, request):
        main_page_categories = self.queryset.filter(main_page_category=True)
        serializer = self.get_serializer(main_page_categories, many=True)
        return Response(serializer.data)


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Knowledge_Center_Article.objects.all()
    serializer_class = KnowledgeCenterArticleSerilizer

    def retrieve(self, request, pk):
        article_in_db = get_object_or_404(self.queryset, pk=pk)
        serializer = self.get_serializer(article_in_db)
        return Response(serializer.data)
