from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from .serializers import MusicsListSerializer, CategoryListSerializer
from .models import Musics, Category


class MusicsListApiView(ListAPIView):
    queryset = Musics.objects.select_related("author")
    serializer_class = MusicsListSerializer
    permission_classes = [IsAuthenticated, ]


class CategoryListApiView(ListAPIView):
    queryset = Category.objects.prefetch_related("musics")
    serializer_class = CategoryListSerializer