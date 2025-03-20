from django.urls import include, path
from .views import *

urlpatterns = [
    path('add-movie', AddMovie.as_view()),
    path('show-all-movies', ShowAllMovies.as_view()),
    path('show-movie', ShowMovie.as_view()),
]