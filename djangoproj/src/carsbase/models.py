from django.db import models
from django.urls import reverse

# Create your models here.
class Basa(models.Model):
    manufacturer = models.CharField(max_length=20)
    model        = models.CharField(max_length=20)
    seats_number = models.IntegerField()
    year         = models.IntegerField()
    drivable     = models.BooleanField()

    def get_absolute_urls(self):
    	return reverse('carsbase:car', kwargs={'id': self.id})

