import uuid
from django.db import models
from cities.models import City
# Create your models here.

class User(models.Model):
    user_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=250, unique=True)
    password = models.CharField(default=0,max_length=500)
    own_city = models.ForeignKey(City, null=True, blank=True , on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=10)
    

    def __str__(self):
        return self.user_name
