from django.core.exceptions import ValidationError
from django.db.migrations.serializer import ModelFieldSerializer
from rest_framework.serializers import ModelSerializer

from apps.models import Category, Blog, Region


class CategoryModelSerializer(ModelSerializer):
    def validate(self, data):
        if Category.objects.filter(name=data['name']).exists():
            raise ValidationError('this name is token')
        return data

    class Meta:
        model = Category
        exclude = ('slug',)


class BlogModelSerializer(ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'


class RegionModelSerializer(ModelSerializer):
    def validate(self, data):
        if Region.objects.filter(name=data['name']).exists():
            raise ValidationError('this name is token')
        return data

    class Meta:
        model = Region
        exclude = ('slug',)
