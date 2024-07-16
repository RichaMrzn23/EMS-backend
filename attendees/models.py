from django.db import models
from users.models import User
from events.models import Event




# Create your models here.
class Attendee(models.Model):
    name = models.ForeignKey(User, on_delete = models.CASCADE, limit_choices_to={'role':'Client'})
    event = models.ForeignKey(Event,related_name='attendees_events', on_delete = models.CASCADE)
    
class Registration(models.Model):
    name = models.ForeignKey(Attendee, on_delete = models.CASCADE)
    event = models.ForeignKey(Event, related_name='registration_events',on_delete = models.CASCADE)
    registration_date = models.DateField(auto_now_add=True)

class Communication(models.Model):
    name = models.ForeignKey(User, on_delete = models.CASCADE)
    event = models.ForeignKey(Event, related_name='communication_events', on_delete = models.CASCADE)
    message = models.TextField()
    message_send_date = models.DateField(auto_now_add= True)