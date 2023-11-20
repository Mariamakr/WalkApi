from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

class Place(models.Model):
    country = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    location = models.CharField(max_length=30)

class Rating(models.Model):
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    stars = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])

    #constrains each user match only with one place - we dont want this here beacause users can visit many places
    # class Meta:
    #     unique_together = (('user', 'place'),)
    #     index_together = (('user', 'place'),)
    #
