from django.shortcuts import get_object_or_404
from rest_framework import response
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import generics, serializers
from rest_framework import mixins
from rest_framework import viewsets
import django_filters.rest_framework
from knowledge_center.models import ArticleRate, KnowledgeCenterArticle, KnowledgeCenterCategory
from knowledge_center.serializers import (
    ArticleRateSerializer,
    KnowledgeCenterArticleSerilizer,
    KnowledgeCenterCategorySerializer,
)


class CategoryAPIView(generics.GenericAPIView, mixins.ListModelMixin, mixins.RetrieveModelMixin):
    queryset = KnowledgeCenterCategory.objects.all()
    serializer_class = KnowledgeCenterCategorySerializer
    lookup_filed = "pk"

    def get(self, request, pk=None):
        if pk:
            return self.retrieve(request, pk)
        return self.list(request)


class CategorySelectedAPIView(viewsets.ModelViewSet):
    queryset = KnowledgeCenterCategory.objects.all()

    @action(detail=False, methods=["get"])
    def selected(self, request):
        main_page_categories = self.queryset.filter(main_page_category=True)
        serializer_context = {'request': request, }
        serializer = KnowledgeCenterCategorySerializer(
            main_page_categories, many=True, context=serializer_context)
        return Response(serializer.data)


class ArticleAPIView(generics.GenericAPIView, mixins.ListModelMixin, mixins.RetrieveModelMixin):
    queryset = KnowledgeCenterArticle.objects.all()
    serializer_class = KnowledgeCenterArticleSerilizer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    lookup_filed = "pk"

    def get(self, request, pk=None):
        if pk:
            return self.retrieve(request, pk)
        return self.list(request)


class ArticleRateViewSet(viewsets.ModelViewSet):
    queryset = ArticleRate.objects.all()
    serializer_class = ArticleRateSerializer

    def create(self, request, pk):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def retrieve(self, request, pk):
        rates = get_object_or_404(self.queryset, pk=pk)
        serializers = self.get_serializer(rates)
        return Response(serializers.data)

