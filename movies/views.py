from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .utils import ValidateMovieDetails, MovieDetails


class AddMovie(APIView):
    def post(self, request):
        payload = request.data
        ValidateMovieDetails.check(payload)
        response = MovieDetails.store_movie(payload)
        return response


class ShowAllMovies(APIView):
    def get(self, request):
        response = MovieDetails.show_all_movies()
        return response


class ShowMovie(APIView):
    def get(self, request):
        payload = request.query_params
        type = payload.get('type')
        if not type or type == '':
            return Response({'message': 'type is misshing', 'status': False}, status=status.HTTP_400_BAD_REQUEST)
        if type == 'id':
            movie_id = payload.get('movie_id')
            response = MovieDetails.show_movie_by_id(movie_id)
        elif type == 'name':
            movie_name = payload.get('movie_name')
            response = MovieDetails.show_movie_by_name(movie_name)
        return response
