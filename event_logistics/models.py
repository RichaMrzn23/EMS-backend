from django.db import models
from events.models import Event
from vendors.models import Vendor
# Create your models here.


class Logistics(models.Model):
    event = models.ManyToManyField(Event)
    name = models.CharField(max_length=100)
    quantity = models.IntegerField()
    price = models.FloatField()
    provided_by = models.ForeignKey(Vendor, on_delete= models.CASCADE)

