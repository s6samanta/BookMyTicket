from django.urls import path
from .views import *

urlpatterns = [
    path('add-city', AddCity.as_view()),
]