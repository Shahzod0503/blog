from rest_framework.parsers import MultiPartParser
from rest_framework.viewsets import ModelViewSet
from django.shortcuts import render

# Create your views here.
from apps.models import Category, Blog, Region
from apps.serializer import CategoryModelSerializer, BlogModelSerializer, RegionModelSerializer


class CategoryModelView(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategoryModelSerializer
    lookup_field = 'slug'


class BlogModelView(ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogModelSerializer
    lookup_field = 'id'
    parser_classes = (MultiPartParser,)


class RegionModelView(ModelViewSet):
    queryset = Region.objects.all()
    serializer_class = RegionModelSerializer
    lookup_field = 'slug'
