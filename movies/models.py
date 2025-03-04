import uuid
from django.db import models

# Create your models here.
class Movie(models.Model):
    movie_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    movie_name = models.CharField(max_length=250)
    movie_genres = models.CharField(max_length=300)
    story = models.TextField()
    lead_actors = models.JSONField(default=list)

    def __str__(self):
        return self.movie_name