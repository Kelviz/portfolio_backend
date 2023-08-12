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


class Skill(models.Model):
    name = models.CharField(max_length=150)
    icon = models.ImageField(upload_to="images")
    bg_color = models.CharField(max_length=200, default="#edf2f8")

    def __str__(self):
        return self.name


class Year(models.Model):
    year = models.CharField(max_length=10)

    def __str__(self):
        return self.year


class Experience(models.Model):
    year = models.ForeignKey(Year, on_delete=models.CASCADE)
    name = models.CharField(max_length=500)
    company = models.CharField(max_length=500)
    description = models.CharField(max_length=1000)

    def __str__(self):
        return self.name


class Testimonial(models.Model):
    name = models.CharField(max_length=500)
    company = models.CharField(max_length=500)
    image = models.ImageField(upload_to="images")
    feedback = models.TextField(max_length=700)

    def __str__(self):
        return self.name


class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
