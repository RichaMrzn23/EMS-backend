from django.db import models
from users.models import User
from events.models import Event


# Create your models here.
class Ticket(models.Model):
    Ticket_Types =(
        ('regular', 'Regular'),
        ('vip', 'VIP')
    )
    event= models.ForeignKey(Event, on_delete= models.CASCADE)
    attendee = models.ForeignKey(User, on_delete=models.CASCADE)
    ticket_type = models.CharField(max_length= 100, choices= Ticket_Types)
    price = models.FloatField()
    purchase_date = models.DateTimeField(auto_now_add= True)
    is_paid = models.BooleanField(default = False)


class Payment(models.Model):
    ticket = models.OneToOneField(Ticket, on_delete = models.CASCADE)
    payment_date = models.DateTimeField(auto_now_add = True)
    amount = models.FloatField()
    payment_method = models.CharField(max_length= 50)
    transaction_id = models.CharField(max_length= 50)
    payment_status = models.CharField(max_length= 50)
    stripe_payment_id = models.CharField(max_length = 50)

    
class Invoice(models.Model):
    payment = models.OneToOneField(Payment, on_delete = models.CASCADE)
    invoice_number = models.CharField(max_length=50)
    created_date = models.DateTimeField(auto_now_add= True)



class Receipt(models.Model):
    invoice  = models.OneToOneField(Invoice, on_delete = models.CASCADE)
    receipt_number = models.CharField(max_length= 50, unique = True)
    created_date = models.DateTimeField(auto_now_add= True)


