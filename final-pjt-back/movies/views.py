from django.shortcuts import render, get_object_or_404, get_list_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Movie, Rating, Genre
from .serializers import MovieListSerializer, MovieSerializer, RatingSerializer
from movies import serializers

# Create your views here.

@api_view(['GET'])
def movies_list(request):
    movies = get_list_or_404(Movie)
    serializer = MovieListSerializer(movies, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def movie_detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializer = MovieSerializer(movie)
    return Response(serializer.data)

@api_view(['POST'])
def create_rating(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    user = request.user

    serializer = RatingSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(movie=movie, user=user)
        ratings = movie.ratings.all()
        serializer = RatingSerializer(ratings, many=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['PUT', 'DELETE'])
def rating_update_or_delete(request, movie_pk, rating_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    rating = get_object_or_404(Rating, pk=rating_pk)

    def update_rating():
        if request.user == rating.user:
            serializer = RatingSerializer(instance=rating, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                ratings = movie.ratings.all()
                serializer = RatingSerializer(ratings, many=True)
                return Response(serializer.data)
    
    def delete_rating():
        if request.user == rating.user:
            rating.delete()
            ratings = movie.ratings.all()
            serializer = RatingSerializer(ratings, many=True)
            return Response(serializer.data)
    
    if request.method == 'PUT':
        return update_rating()
    elif request.method == 'DELETE':
        return delete_rating()
    

