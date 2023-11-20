from django.shortcuts import render
from rest_framework import viewsets
from .models import  Place, Rating
from .serializers import PlaceSerializer, RatingSerializer


class PlaceViewSet(viewsets.ModelViewSet):
    queryset= Place.objects.all()
    serializer_class = PlaceSerializer

class RatingViewSet(viewsets.ModelViewSet):
    queryset= Rating.objects.all()
    serializer_class = RatingSerializer