import uuid

from django.db import models

from cities.models import City


class Hall(models.Model):
    hall_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    hall_name = models.CharField(max_length=250)
    hall_address = models.CharField(max_length=250)
    hall_city = models.ForeignKey(City, on_delete=models.CASCADE)

    def __str__(self):
        return self.hall_name
