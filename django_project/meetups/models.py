from django.db import models
# Create your models here.

class Location(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=300)
    def __str__(self): 
        return f'-- {self.name}'
    
# class Participant(models.Model):
#     name = models.CharField(max_length=200)
#     address = models.CharField(max_length=300)
#     email = models.EmailField(unique=True)
#     def __str__(self):
#         return self.email

class Participant(models.Model):
    email = models.EmailField(unique=True)
    def __str__(self):
        return self.email

class Meetup(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    organizer_email = models.EmailField()
    date = models.DateField()
    description = models.TextField()
    image = models.ImageField(upload_to='images')
    location = models.ForeignKey(Location, null=True, on_delete=models.SET_NULL)
    participants = models.ManyToManyField(Participant, blank=True, null=True)
    def __str__(self): 
        return f'-- {self.title}'