from django.db import models
# Create your models here.

class Location(models.Model):
    name = models. CharField(max_length=200)
    address = models. CharField(max_length=300)


class Meetup(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    image = models.ImageField(upload_to='images')
    location = models.ForeignKey(Location, null=True, on_delete=models.SET_NULL)