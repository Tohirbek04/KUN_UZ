from django.urls import path

from .views_cbv import HomePageView, CategoriesView, RegionsView, NewsView
urlpatterns = [

    path('', HomePageView.as_view(), name='home'),
    path('categories/<slug:slug>', CategoriesView.as_view(), name='categories_news'),
    path('regions/<slug:slug>', RegionsView.as_view(), name='regions_news'),
    path('full_new/<slug:slug>', NewsView.as_view(), name='full_new'),
]
