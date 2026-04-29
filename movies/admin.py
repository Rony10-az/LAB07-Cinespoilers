from django.contrib import admin
from .models import Movie, Genre  # CAMBIO

# NUEVO
@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'release_date', 'is_active', 'created_at')
    search_fields = ('title',)
    list_filter = ('is_active', 'release_date')
    ordering = ('-created_at',)

    # NUEVO
    filter_horizontal = ('genres',)  # IMPORTANTE: mejora UI para ManyToMany