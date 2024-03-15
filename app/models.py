from django.db import models
from django.utils.text import slugify


class BaseModel(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, blank=True)

    class Meta:
        abstract = True


class Categories(BaseModel):

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Categories, self).save(*args, **kwargs)


class Regions(BaseModel):

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Regions, self).save(*args, **kwargs)


class News(models.Model):
    title = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, blank=True)
    description = models.TextField(blank=True)
    image = models.ImageField(blank=True, null=True)
    join_date = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE, blank=True, null=True)
    region = models.ForeignKey(Regions, on_delete=models.CASCADE, blank=True, null=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(News, self).save(*args, **kwargs)
