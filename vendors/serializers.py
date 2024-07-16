
from rest_framework import serializers
from .models import *


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields= '__all__'


class VendorSerializer(serializers.ModelSerializer):
    service_offered = ServiceSerializer(many = True, read_only = True)
    class Meta:
        model = Vendor
        fields = '__all__'

