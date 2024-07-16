from django.shortcuts import render
from .models import Review
from.serializers import ReviewSerializer
from rest_framework.viewsets import ModelViewSet


# Create your views here.

class ReviewView(ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer