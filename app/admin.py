from django.contrib import admin

from app.models import Categories, Regions, News

admin.site.register([Categories, Regions, News])


