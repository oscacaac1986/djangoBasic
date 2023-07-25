from django.db import models

# Create your models here.


class VehicleModel(models.Model):
    
    placa= models.CharField(max_length=6)
    color = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    marca = models.CharField(max_length=100)
    
