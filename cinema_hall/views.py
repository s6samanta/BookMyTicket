from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import request, status
from rest_framework.response import Response


class AddHall(APIView):
    def post(self, request):
        data = request.data
        
        return Response({'message':'data inserted successfully', 'status': True}, status=status.HTTP_200_OK)
