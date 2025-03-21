from .models import Hall
from .serializer import HallSerializer

from rest_framework import status
from rest_framework.response import Response


class HallOperations:
    @classmethod
    def show_hall_by_city(cls, city_name):
        if not city_name or city_name == '':
            return Response({'message': 'city_name is missing', 'status': False}, status=status.HTTP_400_BAD_REQUEST)
        hall_data = Hall.objects.filter(hall_city__city_name=city_name)
        data = [
            {    
                'hall_name': each_hall.hall_name,
                'hall_address': each_hall.hall_address,
                'hall_city': each_hall.hall_city.city_name,
            }
            for each_hall in hall_data
        ]
        return Response({'data': data, 'status': True}, status=status.HTTP_200_OK)

    @classmethod
    def show_hall_by_hall_name(cls, hall_name):
        if not hall_name or hall_name == '':
            return Response({'message': 'hall_name is missing', 'status': False}, status=status.HTTP_400_BAD_REQUEST)
        hall_data = Hall.objects.select_related('hall_city').filter(hall_name__icontains=hall_name)
        data = [
            {    
                'hall_name': each_hall.hall_name,
                'hall_address': each_hall.hall_address,
                'hall_city': each_hall.hall_city.city_name,    
            }
            for each_hall in hall_data
        ]
        return Response({'data': data, 'status': True}, status=status.HTTP_200_OK)
