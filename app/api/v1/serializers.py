from rest_framework import serializers

from app.models import Categories, News, Regions


class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = ['id', 'name']


class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Regions
        fields = ['id', 'name']


class NewsSerializer(serializers.ModelSerializer):
    category = CategorySerializers(read_only=True)
    region = RegionSerializer(read_only=True)

    class Meta:
        model = News
        fields = '__all__'


class CreateNewsSerializer(serializers.ModelSerializer):

    class Meta:
        model = News
        fields = ['title', 'description', 'image', 'category', 'region']


class UpdateNewsSerializer(serializers.ModelSerializer):

    class Meta:
        model = News
        fields = ['title', 'description', 'image']





