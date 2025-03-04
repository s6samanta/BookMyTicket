from django.urls import include, path
from .views import *

urlpatterns = [
    path('add-movie', AddMovie.as_view())
]