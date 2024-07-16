from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('event_planner', 'Event Planner'),
        ('vendor', 'Vendor'),
        ('client', 'Client'),
    )
    email = models.EmailField(unique = True)
    role = models.CharField(max_length=50, choices=ROLE_CHOICES)
    password = models.CharField(max_length = 100)
    username = models.CharField(max_length = 50, default = 'username')
    
    USERNAME_FIELD ='email'
    REQUIRED_FIELDS = ['username']


    
    def __str__(self):
        return self.email
    

