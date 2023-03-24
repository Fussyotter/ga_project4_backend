from django.shortcuts import render
from rest_framework import generics
from .serializers import ArticleSerializer
from .models import Article

class ArticleList(generics.ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

class ArticleDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
# Create your views here.
