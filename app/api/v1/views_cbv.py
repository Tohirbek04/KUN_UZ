from rest_framework import mixins, generics
from rest_framework import filters
from app.api.v1.serializers import NewsSerializer, CreateNewsSerializer, UpdateNewsSerializer
from app.models import News


class NewsListAPIView(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title']

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class NewsDeleteRetrieveAPIView(mixins.DestroyModelMixin, mixins.RetrieveModelMixin, generics.GenericAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class CreateAPIView(mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class NewsUpdateView(mixins.UpdateModelMixin, generics.GenericAPIView):
    queryset = News.objects.all()
    serializer_class = UpdateNewsSerializer

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
