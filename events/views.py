from django.shortcuts import render
from .models import Event, Category
from .serializers import EventSerializer, CategorySerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework import filters
from rest_framework.permissions import DjangoModelPermissions

# Create your views here.

class EventView(ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    filterset_fields = ['category', 'Event_Planner']
    search_fields = ['title']
    
class CategoryView(ModelViewSet):
    queryset =Category .objects.all()
    serializer_class = CategorySerializer




