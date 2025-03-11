import uuid
from django.db import models

# Create your models here.
class City(models.Model):
    city_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    city_name = models.CharField(max_length=250, unique=True)

    def __str__(self):
        return self.city_name
