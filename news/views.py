from rest_framework import viewsets
from .serializers import CategorySerializer, NewsSerializer
from .models import Category, News

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    pagination_by = 5

class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    pagination_by = 5