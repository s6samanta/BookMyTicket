import bcrypt
from email_validator import validate_email, EmailNotValidError

from rest_framework import status
from django.shortcuts import render
from django.db import IntegrityError
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import User
from cities.models import City
from .validators import Validate


class Signup(APIView):
    def post(self, request):
        data = request.data.dict()
        Validate.is_valiadate(
            user_name=data.get("user_name"),
            email=data.get("email"),
            password=data.get("password"),
            own_city=data.get("own_city"),
            phone_number=data.get("phone_number"),
        )
        city_id = data.get("own_city")
        try:
            city_instance = City.objects.get(city_id=city_id)
        except:
            return Response({'message':'enter valid city', 'status':False}, status=status.HTTP_400_BAD_REQUEST)
        
        data["own_city"] = city_instance
        try:
            User.objects.create(**data)
        except IntegrityError as e:
            return Response({'message':'user already exists', 'status': False}, status=status.HTTP_400_BAD_REQUEST)
        
        password = bcrypt.hashpw(data.get('password').encode(), salt=bcrypt.gensalt())
        data["password"] = password
        return Response(
            {"message": "User created successfully"}, status=status.HTTP_201_CREATED
        )
    
