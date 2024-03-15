from app.models import Categories, Regions


def categories(request):
    categories = Categories.objects.all()
    return {'categories': categories}


def regions(request):
    regions = Regions.objects.all()
    return {'regions': regions}
