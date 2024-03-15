from django.urls import path

from app.api.v1.views import news_method, news_detail

from app.api.v1.views_cbv import NewsListCreateAPIView, NewsDeleteRetrieveAPIView, NewsUpdateView

urlpatterns = [
    path('news/', news_method, name='news'),
    path('news/<int:id>', news_detail, name='news_detail'),
]

klass = [
    path('news/', NewsListCreateAPIView.as_view(), name='news-list'),
    path('news/<int:pk>', NewsDeleteRetrieveAPIView.as_view(), name='news'),
    path('news-update/<int:pk>', NewsUpdateView.as_view(), name='news_update'),
]

urlpatterns += klass