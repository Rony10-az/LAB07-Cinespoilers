from rest_framework import serializers
from .models import Movie, Genre

# NUEVO
class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'


class MovieSerializer(serializers.ModelSerializer):
    # NUEVO
    genres = GenreSerializer(many=True, read_only=True)

    # NUEVO
    genre_ids = serializers.PrimaryKeyRelatedField(
        queryset=Genre.objects.all(),
        many=True,
        write_only=True
    )

    class Meta:
        model = Movie
        fields = [
            "id",
            "title",
            "description",
            "release_date",
            "is_active",
            "created_at",
            "genres",     # 👈 ahora queda al final
            "genre_ids"   # (solo entrada, no se verá en respuesta)
        ]

    # NUEVO
    def create(self, validated_data):
        genres = validated_data.pop('genre_ids', [])
        movie = Movie.objects.create(**validated_data)
        movie.genres.set(genres)
        return movie

    # NUEVO
    def update(self, instance, validated_data):
        genres = validated_data.pop('genre_ids', None)
        instance = super().update(instance, validated_data)
        if genres is not None:
            instance.genres.set(genres)
        return instance