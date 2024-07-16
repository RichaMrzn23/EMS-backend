from django.contrib import admin
from .models import Attendance_Report, Revenue_Report, Vendor_Performance_Report
# Register your models here.

admin.site.register(Attendance_Report)
admin.site.register(Revenue_Report)
admin.site.register(Vendor_Performance_Report)
