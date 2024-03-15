from app.models import News, Categories, Regions
from django.views import View
from django.shortcuts import render, get_object_or_404


class HomePageView(View):

    def get(self, request, *args, **kwargs): # noqa
        news = News.objects.all().order_by('-id')[:10]
        return render(request, 'base.html', {'news': news})


class CategoriesView(View):

    def get(self, request, slug, *args, **kwargs): # noqa

        category = get_object_or_404(Categories, slug=slug)
        news = News.objects.filter(category=category)
        context = {
            'category': category,
            'news': news
        }
        return render(request, 'categories_news.html', context=context)


class RegionsView(View):

    def get(self, request, slug, *args, **kwargs): # noqa

        region = get_object_or_404(Regions, slug=slug)
        news = News.objects.filter(region=region)

        context = {
            'news': news,
            'region': region
        }
        return render(request, 'regions.html', context=context)


class NewsView(View):

    def get(self, request, slug, *args, **kwargs): # noqa

        news = News.objects.get(slug=slug)
        return render(request, 'full_new.html', {'news': news})












