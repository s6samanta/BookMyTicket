import json
import uuid

from rest_framework import status
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError

from .models import Movie
from .serializer import MovieSerializer


class ValidateMovieDetails:
    @classmethod
    def check(cls, movie_data):
        keys = ['movie_name', 'movie_genres', 'story', 'lead_actors']
        for key in keys:
            if not movie_data.get(key) or movie_data.get(key) == '':
                raise ValidationError({'message': f'{key} is missing or invalid.', 'status': False})


class MovieDetails:
    @classmethod
    def store_movie(cls, movie_data):
        Movie.objects.create(movie_name=movie_data.get('movie_name'), movie_genres=movie_data.get('movie_genres'), story=movie_data.get('story'), lead_actors=json.loads(movie_data.get('lead_actors')))
        return Response({'message': 'data inserted successfully', 'status':True}, status=status.HTTP_201_CREATED)

    @classmethod
    def show_all_movies(cls):
        fields_to_include = ['movie_name', 'movie_genres', 'lead_actors', 'story']
        movies = Movie.objects.values(*fields_to_include)
        return Response({'data': list(movies), 'status': True}, status=status.HTTP_200_OK)

    @classmethod
    def show_movie_by_id(cls, movie_id):
        if movie_id:
            try:
                uuid.UUID(movie_id)
            except:
                return Response({'message': 'invalid movie_id', 'status': False}, status=status.HTTP_400_BAD_REQUEST)

            movie_data = MovieSerializer(Movie.objects.filter(movie_id=movie_id), many=True).data
            if movie_data != []:
                return Response({'movie_data': movie_data, 'status': True}, status=status.HTTP_200_OK)
            return Response({'message': 'There is no movie for this particular id', 'status': False}, status=status.HTTP_204_NO_CONTENT)
        return Response({'message': 'movie_id is missing', 'status': False}, status=status.HTTP_400_BAD_REQUEST)

    @classmethod
    def show_movie_by_name(cls, movie_name):
        if movie_name:
            movie_data = MovieSerializer(Movie.objects.filter(movie_name__icontains=movie_name), many=True).data
            return Response({'movie_data': movie_data, 'status': True}, status=status.HTTP_200_OK)
        return Response({'message': 'movie_name is missing', 'status': False}, status=status.HTTP_400_BAD_REQUEST)
