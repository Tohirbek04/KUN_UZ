from django.urls import path
from app.views import home, categories_news, regions_news, full_new

urlpatterns = [
    path('', home, name='home'),
    path('categories/<slug:slug>', categories_news, name='categories_news'),
    path('regions/<slug:slug>', regions_news, name='regions_news'),
    path('full_new/<slug:slug>', full_new, name="full_new")
]








