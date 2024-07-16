from django.contrib import admin
from .models import Attendee, Registration, Communication
# Register your models here.

admin.site.register(Attendee)
admin.site.register(Registration)
admin.site.register(Communication)