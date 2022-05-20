from django.db import models

# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=100)

class Movie(models.Model):
    
    title = models.CharField(max_length=100)
    overview = models.TextField()
    poster_path = models.TextField()
    release_date = models.DateTimeField()
    genre_ids = models.ManyToManyField(Genre, related_name="genre_movies")
