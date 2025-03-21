from .utils import HallOperations

from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import request, status
from rest_framework.response import Response

class CityHallViewer(APIView):
    def get(self, request):
        payload = request.query_params
        search_by = payload.get('search_by')
        if not search_by or search_by == '':
            return Response({'message': 'search_by is missing', 'status': False}, status=status.HTTP_400_BAD_REQUEST)
        if search_by == 'city_name':
            response = HallOperations.show_hall_by_city(payload.get('city_name'))
        elif search_by == 'hall_name':
            response = HallOperations.show_hall_by_hall_name(payload.get('hall_name'))
        else:
            return Response({'message': 'invalid search type', 'status': False}, status=status.HTTP_400_BAD_REQUEST)
        
        return response
