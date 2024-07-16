from django.contrib import admin
from .models import Ticket, Payment, Invoice, Receipt
# Register your models here.

admin.site.register(Ticket)
admin.site.register(Payment)
admin.site.register(Invoice)
admin.site.register(Receipt)
