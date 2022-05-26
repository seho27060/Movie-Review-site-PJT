from rest_framework import serializers
from .models import Movie, Genre, Rating
from django.contrib.auth import get_user_model

User = get_user_model()

class RatingSerializer(serializers.ModelSerializer):

    class UserSerializer(serializers.ModelSerializer):

        class Meta:
            model = User
            fields = ('pk', 'username')
    
    user = UserSerializer(read_only=True)

    class Meta:
        model = Rating
        fields = ('pk','rating','user','movie')
        read_only_fields = ('movie',)

class MovieListSerializer(serializers.ModelSerializer):

    ratings = RatingSerializer(many=True, read_only=True)
    
    class Meta:
        model = Movie
        fields = ('pk','poster_path', 'title', 'ratings')

class MovieSerializer(serializers.ModelSerializer):

    class GenreSerializer(serializers.ModelSerializer):

        class Meta:
            model = Genre
            fields = ('pk','name',)

    genre_ids = GenreSerializer(many=True, read_only=True)
    ratings = RatingSerializer(many=True, read_only=True)
    
    class Meta:
        model = Movie
        fields = ('pk','genre_ids', 'title', 'overview','poster_path','release_date','ratings')




