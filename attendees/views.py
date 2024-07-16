from django.shortcuts import render
from .models import *
from .serializers import AttendeeSerializer, RegistrationSerializer, CommunicationSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response


# Create your views here.

class AttendeeView(ModelViewSet):
    queryset = Attendee.objects.all()
    serializer_class = AttendeeSerializer

class RegistrationView(GenericAPIView):
    queryset = Registration.objects.all()
    serializer_class = RegistrationSerializer

    def list(self, request):
        queryset = self.get_queryset()
        serialiser = self.serializer_class(queryset, many = True)
        return Response(serialiser.data)
    
    def create(self, serializer):
        event = serializer.validated_data['event']
        event.attendee_count += 1
        event.save()
        serializer.save()

class CommunicationView(ModelViewSet):
    queryset = Communication.objects.all()
    serializer_class = CommunicationSerializer

