from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializers import *

# Create your views here.
class Attendance_ReportView(ModelViewSet):
    queryset = Attendance_Report.objects.all()
    serializer_class = Attendance_ReportSerializer

    
class Revenue_ReportView(ModelViewSet):
    queryset = Revenue_Report.objects.all()
    serializer_class = Revenue_ReportSerializer


class Vendor_Performance_ReportView(ModelViewSet):
    queryset = Vendor_Performance_Report.objects.all()
    serializer_class = Vendor_Performance_ReportSerializer