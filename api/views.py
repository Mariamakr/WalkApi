from django.shortcuts import render
from rest_framework import viewsets, status
from .models import  Place, Rating
from .serializers import PlaceSerializer, RatingSerializer
from rest_framework.response import Response
from rest_framework.decorators import action

class PlaceViewSet(viewsets.ModelViewSet):
    queryset= Place.objects.all()
    serializer_class = PlaceSerializer

    @action(detail=True, methods=['POST'])
    def rate_place(self,request, pk=None):
        response = {'message': 'is working'}
        return Response(response, status=status.HTTP_200_OK)


class RatingViewSet(viewsets.ModelViewSet):
    queryset= Rating.objects.all()
    serializer_class = RatingSerializer