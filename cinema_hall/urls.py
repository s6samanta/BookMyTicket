from django.urls import include, path
from .views import *

urlpatterns = [
    path('show-hall', CityHallViewer.as_view()),
]