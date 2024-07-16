from django.db import models
from events.models import Event
from users.models import User
# Create your models here.

class Review(models.Model):
    event = models.ForeignKey(Event, on_delete= models.CASCADE)
    reviewer = models.ForeignKey(User, on_delete = models.CASCADE, limit_choices_to={'role':'client'})
    feedback = models.TextField()
    rating = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)