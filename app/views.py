from django.shortcuts import render

from app.models import News, Categories, Regions


def home(request):
    news = News.objects.all().order_by('-id')[:10]
    context = {
        'news': news
    }
    return render(request, 'base.html', context)


def categories_news(request, slug):
    category = Categories.objects.get(slug=slug)
    news = News.objects.filter(category=category)
    context = {
        'news': news,
        'category': category
    }
    return render(request, 'categories_news.html', context)


def regions_news(request, slug):
    region = Regions.objects.get(slug=slug)
    news = News.objects.filter(region=region)
    context = {
        'news': news,
        'region': region
    }
    return render(request, 'regions.html', context)


def full_new(request, slug):
    new = News.objects.get(slug=slug)

    context = {'new': new}

    return render(request, 'full_new.html', context)
