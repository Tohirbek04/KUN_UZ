from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from app.api.v1.serializers import NewsSerializer, CreateNewsSerializer,  UpdateNewsSerializer
from app.models import News


@api_view(http_method_names=['GET', 'POST'])
def news_method(request):
    if request.method == 'GET':
        news = News.objects.all()
        serializer = NewsSerializer(news, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    if request.method == 'POST':
        serializer = CreateNewsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(http_method_names=['GET', 'DELETE'])
def news_detail(request, id):  # noqa
    if request.method == 'GET':
        news = get_object_or_404(News, id=id)
        serializer = NewsSerializer(news)
        return Response(serializer.data, status=status.HTTP_200_OK)

    if request.method == 'DELETE':
        new = get_object_or_404(News, id=id)
        new.delete()
        return Response(status=status.HTTP_205_RESET_CONTENT)

    if request.method == 'PUT':
        new = get_object_or_404(News, id=id)
        update_new = UpdateNewsSerializer(new, data=request.data)
        if update_new.is_valid():
            update_new.save()
            return Response(status=status.HTTP_200_OK)
        return Response(update_new.errors, status=status.HTTP_400_BAD_REQUEST)




