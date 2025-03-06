import uuid
from django.db import models
from movies.models import Movie
from cinema_hall.models import Hall 

# Create your models here.

class Ticket(models.Model):
    ticket_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    cinema_hall = models.ForeignKey(Hall, on_delete=models.CASCADE)
    ticket_price = models.DecimalField(max_digits=3, decimal_places=0)
    show_time = models.DateTimeField()
    booked_at = models.DateTimeField(auto_now_add=True)
