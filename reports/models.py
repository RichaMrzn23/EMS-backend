from django.db import models
from events.models import Event
from attendees.models import Registration
from reviews_feedbacks.models import Review
from vendors.models import Vendor

# Create your models here.
class Attendance_Report(models.Model):
    event = models.ForeignKey(Event, on_delete= models.CASCADE)
    total_attendees = models.ForeignKey(Registration, on_delete= models.CASCADE)
    rating = models.ForeignKey(Review, on_delete= models.CASCADE)
    report_generated_date = models.DateTimeField(auto_now_add= True)
    

class Revenue_Report(models.Model):
    event = models.ForeignKey(Event, on_delete= models.CASCADE)
    total_revenue = models.IntegerField()
    report_generated_date = models.DateTimeField(auto_now_add= True)

class Vendor_Performance_Report(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete= models.CASCADE)
    total_event_served = models.IntegerField()
    rating = models.IntegerField()
    report_generated_date = models.DateTimeField(auto_now_add= True)
    