from django.urls import include, path
from .views import *

urlpatterns = [
    path('signup', Signup.as_view()),
    path('login', Login.as_view()),
]