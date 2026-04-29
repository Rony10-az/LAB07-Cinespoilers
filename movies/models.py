from django.db import models

# NUEVO
class Genre(models.Model):
    name = models.CharField(max_length=100, unique=True)  # IMPORTANTE: único

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    release_date = models.DateField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    # NUEVO
    genres = models.ManyToManyField(Genre, related_name='movies', blank=True)

    def __str__(self):
        return self.title