
from django.shortcuts import render
from .models import *
from rest_framework.viewsets import ModelViewSet
from .serializers import ServiceSerializer, VendorSerializer

# Create your views here.


class ServiceView(ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    
class VendorView(ModelViewSet):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer
    