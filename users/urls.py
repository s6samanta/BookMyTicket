from django.urls import include, path
from .views import *

urlpatterns = [
    path('signup', Signup.as_view())
]