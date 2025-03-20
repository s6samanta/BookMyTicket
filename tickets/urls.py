from django.contrib import admin
from django.urls import path, include

from .views import ShowTicketDetails

urlpatterns = [
    path('ticket-details', ShowTicketDetails.as_view()),
]