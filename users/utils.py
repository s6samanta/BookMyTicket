import bcrypt

from .models import User
from django.http import HttpResponse, HttpResponseBadRequest, JsonResponse
from rest_framework import status
from rest_framework.response import Response

from .serializer import UserSerializer


class UserOperations:
    @classmethod
    def login_operations(cls, email, password):
        user_data = UserSerializer(User.objects.get(email=email)).data
        if not user_data:
            return Response({'message': 'user not found', 'status': False}, status=status.HTTP_400_BAD_REQUEST)
        if bcrypt.checkpw(password.encode(), user_data.get('password').split("'")[1].encode()):
            return Response({'message': 'You have logged in successfully', 'status': True}, status=status.HTTP_200_OK)
        return Response({'message': 'invalid email or password', 'status': False}, status=status.HTTP_400_BAD_REQUEST)