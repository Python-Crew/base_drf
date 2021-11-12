from django.shortcuts import get_object_or_404
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import viewsets
from django_filters import rest_framework as filters
from knowledge_center.filter import ArticleFilter, CategoryFilter
from knowledge_center.models import (
    ArticleRate,
    KnowledgeCenterArticle,
    KnowledgeCenterCategory,
)
from knowledge_center.serializers import (
    ArticleRateSerializer,
    KnowledgeCenterArticleSerilizer,
    KnowledgeCenterCategorySerializer,
)


class CategoryListAPIView(generics.ListAPIView):
    queryset = KnowledgeCenterCategory.objects.all()
    serializer_class = KnowledgeCenterCategorySerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = CategoryFilter


class CategoryDetailAPIView(generics.RetrieveAPIView):
    queryset = KnowledgeCenterCategory.objects.all()
    serializer_class = KnowledgeCenterCategorySerializer
    lookup_filed = "pk"

    def get(self, request, **kwargs):
        cat_title = self.get_object()
        articles = KnowledgeCenterArticle.objects.filter(
            category__in=KnowledgeCenterCategory.objects.get(
                title=cat_title
            ).get_descendants(include_self=True)
        )
        filter_articles = ArticleFilter(self.request.GET, queryset=articles)
        serializer = KnowledgeCenterCategorySerializer(
            filter_articles.qs, many=True, context={"request": request}
        )

        return Response(serializer.data)


class CategorySelectedAPIView(viewsets.ModelViewSet):
    queryset = KnowledgeCenterCategory.objects.all()

    @action(detail=False, methods=["get"])
    def selected(self, request):
        main_page_categories = self.queryset.filter(main_page_category=True)
        serializer_context = {
            "request": request,
        }
        serializer = KnowledgeCenterCategorySerializer(
            main_page_categories, many=True, context=serializer_context
        )
        return Response(serializer.data)


class ArticleListAPIView(generics.ListAPIView):
    queryset = KnowledgeCenterArticle.objects.all()
    serializer_class = KnowledgeCenterArticleSerilizer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = ArticleFilter


class ArticleDetailAPIView(generics.RetrieveAPIView):
    queryset = KnowledgeCenterArticle.objects.all()
    serializer_class = KnowledgeCenterArticleSerilizer
    lookup_filed = "pk"


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
