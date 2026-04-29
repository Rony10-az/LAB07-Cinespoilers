from rest_framework import serializers
from .models import Review

class ReviewSerializer(serializers.ModelSerializer):

    # NUEVO
    def validate_rating(self, value):
        if value < 1 or value > 5:
            raise serializers.ValidationError("El rating debe estar entre 1 y 5")
        return value

    class Meta:
        model = Review
        fields = '__all__'