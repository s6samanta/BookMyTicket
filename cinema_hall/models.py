import uuid
from movies.models import Movie
from django.db import models
from django.core.validators import MaxLengthValidator, MinValueValidator

# Create your models here.

class Hall(models.Model):
    hall_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    hall_name = models.CharField(max_length=250)
    hall_address = models.CharField(max_length=250)
    hall_city = models.CharField(max_length=250)
    # movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.hall_name
