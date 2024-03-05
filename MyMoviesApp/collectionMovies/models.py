from django.db import models

# Create your models here.
from django.db import models

class Collection(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    genres = models.CharField(max_length=100)
    uuid = models.CharField(max_length=100)

class CollectionMovie(models.Model):
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

class RequestCounter(models.Model):
    counter = models.IntegerField(default=0)

    def increment(self):
        self.counter += 1
        self.save()

    def reset(self):
        self.counter = 0
        self.save()