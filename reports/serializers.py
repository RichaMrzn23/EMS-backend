from .models import Attendance_Report, Revenue_Report, Vendor_Performance_Report
from rest_framework import serializers

class Attendance_ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance_Report
        fields = '__all__'


class Revenue_ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Revenue_Report
        fields = '__all__'

class Vendor_Performance_ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor_Performance_Report
        fields = '__all__'