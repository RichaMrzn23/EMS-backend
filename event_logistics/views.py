from django.shortcuts import render
from .models import Logistics
from .serializers import LogisticsSerializer
from rest_framework.viewsets import ModelViewSet

# Create your views here.

class LogisticsView(ModelViewSet):
    queryset = Logistics.objects.all()
    serializer_class = LogisticsSerializer