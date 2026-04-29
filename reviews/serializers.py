from rest_framework import serializers
from .models import Review
from movies.models import Movie  # IMPORTANTE

# NUEVO → serializer simple de movie (lectura)
class MovieSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['id', 'title']  # IMPORTANTE


class ReviewSerializer(serializers.ModelSerializer):

    # NUEVO → lectura (objeto)
    movie = MovieSimpleSerializer(read_only=True)

    # NUEVO → escritura (ID)
    movie_id = serializers.PrimaryKeyRelatedField(
        queryset=Movie.objects.all(),
        source='movie',
        write_only=True
    )

    def validate_rating(self, value):
        if value < 1 or value > 5:
            raise serializers.ValidationError("El rating debe estar entre 1 y 5")
        return value

    class Meta:
        model = Review
        fields = '__all__'