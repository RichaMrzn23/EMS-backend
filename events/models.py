from django.db import models
from users.models import User

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length = 100)

class Event(models.Model):
    title = models.CharField(max_length = 100)
    datetime = models.DateTimeField()
    location = models.CharField(max_length = 100)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete = models.SET_NULL, null= True)
    Event_Planner = models.ForeignKey(User, on_delete = models.CASCADE, limit_choices_to={'role': 'event_planner'})
    attendee_count = models.PositiveIntegerField(default = 0)