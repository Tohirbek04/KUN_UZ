from django.urls import path

from app.api.v1.views import news_method, news_detail

from app.api.v1.views_cbv import NewsListAPIView, NewsDeleteRetrieveAPIView, NewsUpdateView, CreateAPIView

urlpatterns = [
    path('news/', news_method, name='news'),
    path('news/<int:id>', news_detail, name='news_detail'),
]

klass = [
    path('news/', NewsListAPIView.as_view(), name='news-list'),
    path('news/<int:pk>', NewsDeleteRetrieveAPIView.as_view(), name='news'),
    path('news-create/<int:pk>', CreateAPIView.as_view(), name='news-create'),
    path('news-update/<int:pk>', NewsUpdateView.as_view(), name='news_update'),
]

urlpatterns += klass