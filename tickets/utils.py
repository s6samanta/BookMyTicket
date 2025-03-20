import uuid

from rest_framework import status
from rest_framework.response import Response
from django.core.exceptions import ValidationError 

from .models import Ticket
from .serializer import TicketSerializer


class TicketDetails:
    @classmethod
    def get_ticket_details(cls, ticket_id):
        try:
            uuid.UUID(ticket_id)
        except Exception as e:
            return Response({'message': 'invalid ticket id', 'status': False}, status=status.HTTP_400_BAD_REQUEST)
        try:
            ticket = Ticket.objects.select_related('movie', 'cinema_hall').get(ticket_id=ticket_id)
            print(ticket)
            data = {
                'ticket_id': str(ticket.ticket_id),
                'movie_name': ticket.movie.movie_name,
                'cinema_hall_name': ticket.cinema_hall.hall_name,
                'cinema_hall_address': ticket.cinema_hall.hall_address,
                'cinema_hall_city': ticket.cinema_hall.hall_city.city_name,
                'ticket_price': ticket.ticket_price,
                'show_time': ticket.show_time,
                'booked_at': ticket.booked_at,
            }
            return Response({'ticket_details': data, 'status': True}, status=status.HTTP_200_OK)
        except Ticket.DoesNotExist:
            return Response({'message': 'Ticket not found', 'status': False}, status=status.HTTP_204_NO_CONTENT)
            
