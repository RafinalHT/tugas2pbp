from turtle import title
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.
class MyWatchlist(models.Model):
    watched = models.BooleanField(default=False)
    title = models.CharField(max_length=100)
    # Create rating from 1-5
    rating = models.IntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(5)])
    release_date = models.DateField()
    review = models.TextField()