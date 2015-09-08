from django.shortcuts import render
from rest_framework import viewsets

from .models import Quote, Article
from .serializers import QuoteSerializer, ArticleSerializer


class QuoteViewSet(viewsets.ModelViewSet):
    serializer_class = QuoteSerializer
    queryset = Quote.objects.all()


class ArticleViewSet(viewsets.ModelViewSet):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()
