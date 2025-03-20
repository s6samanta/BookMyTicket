from .models import City

from rest_framework import status
from django.db import IntegrityError
from rest_framework.response import Response


class CityDetails:
    @classmethod
    def add_city(cls, city_name):
        if not city_name or city_name == '':
            return Response({'message': 'city name is missing', 'status': False }, status=status.HTTP_400_BAD_REQUEST)
        try:
            City.objects.create(city_name=city_name)
        except IntegrityError:
            return Response({'message': 'city already exists', 'status': False}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'message': 'You have successfully added the city', 'status': True}, status=status.HTTP_201_CREATED)
    
