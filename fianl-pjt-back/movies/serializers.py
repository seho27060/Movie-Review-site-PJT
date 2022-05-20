from rest_framework import serializers
from .models import Movie, Genre, Rating


class MovieListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ('poster_path', 'title')

class MovieSerializer(serializers.ModelSerializer):

    class GenreSerializer(serializers.ModelSerializer):

        class Meta:
            model = Genre
            fields = ('pk','name',)
    
    class RatingSerializer(serializers.ModelSerializer):

        class Meta:
            model = Rating
            fields = ('pk','score',)

    scores = RatingSerializer(many=True)
    genre_ids = GenreSerializer(many=True, read_only=True)

    class Meta:
        model = Movie
        fields = ('scores', 'genre_ids', 'title', 'overview','poster_path','release_date',)