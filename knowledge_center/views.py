from knowledge_center.serializers import CategorySerializer
from .models import *
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404
from rest_framework import status, viewsets

# Create your views here.


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def retrieve(self,request,pk):
        categories_in_db = get_object_or_404(self.queryset,pk=pk)
        serializer = self.get_serializer(categories_in_db)
        if serializer:
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

