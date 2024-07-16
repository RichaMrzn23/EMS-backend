from django.db import models
from users.models import User



# Create your models here.
class Service(models.Model):
    name = models.CharField(max_length = 100)
    description = models.TextField()

class Vendor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, limit_choices_to={'role': 'vendor'})
    company_name = models.CharField(max_length = 100)
    address = models.CharField(max_length = 100)
    contact_number = models.IntegerField()
    service_offered = models.ManyToManyField(Service, related_name = 'vendors')
    