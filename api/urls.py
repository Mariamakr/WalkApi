from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from django.conf.urls import include
from .views import PlaceViewSet, RatingViewSet

router = routers.DefaultRouter()
router.register('places', PlaceViewSet)
router.register('ratings', RatingViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

