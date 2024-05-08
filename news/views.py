from django.shortcuts import render
from django.core.paginator import Paginator
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status, viewsets
from .serializers import NewsSerializer
from .models import News


class NewsViewSet(viewsets.ModelViewSet):

    queryset = News.objects.all()
    serializer_class = NewsSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]