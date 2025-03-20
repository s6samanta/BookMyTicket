from .utils import CityDetails

from rest_framework import status 
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response


class AddCity(APIView):
    def post(self, request):
        payload = request.data
        response = CityDetails.add_city(payload.get('city_name'))
        return response

