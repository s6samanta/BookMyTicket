from django.urls import include, path
from .views import *

urlpatterns = [
    path('add-hall', AddHall.as_view())
]