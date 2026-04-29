from django.db import models
from movies.models import Movie  # IMPORTANTE

# CAMBIO
class Review(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='reviews')

    reviewer_name = models.CharField(max_length=100)

    # NUEVO
    reviewer_email = models.EmailField()

    # NUEVO
    title = models.CharField(max_length=150)

    # CAMBIO
    rating = models.IntegerField()

    comment = models.TextField()

    # NUEVO
    is_active = models.BooleanField(default=True)  # moderación simple

    created_at = models.DateTimeField(auto_now_add=True)

    # NUEVO
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.reviewer_name} - {self.movie.title}"