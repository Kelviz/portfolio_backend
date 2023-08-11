from django.db import models
from autoslug import AutoSlugField

# Create your models here.


class About(models.Model):
    title = models.CharField(max_length=1000)
    description = models.TextField()
    image = models.ImageField(upload_to="images")

    def __str__(self):
        return self.title


class Tag(models.Model):
    name = models.CharField(max_length=500)
    slug = AutoSlugField(populate_from='name',
                         max_length=100, unique=True, null=True)

    def __str__(self):
        return self.name


class Work(models.Model):
    title = models.CharField(max_length=1500)
    description = models.TextField()
    project_link = models.CharField(max_length=2000)
    code_link = models.CharField(max_length=2000)
    image = models.ImageField(upload_to="images")
    tag = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title
