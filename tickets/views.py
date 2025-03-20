from rest_framework import status
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from .utils import TicketDetails


class ShowTicketDetails(APIView):
    def get(self, request):
        payload = request.query_params
        if not payload.get('ticket_id'):
            return Response({'message': 'ticket id is missing', 'status': False}, status=status.HTTP_400_BAD_REQUEST)
        response = TicketDetails.get_ticket_details(payload.get('ticket_id'))
        return response