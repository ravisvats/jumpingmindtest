from django.db import models

class Elevator(models.Model):
    floor = models.IntegerField()
    direction = models.CharField(max_length=10)
    status = models.CharField(max_length=10)
    maintenance = models.BooleanField(default=False)

class Request(models.Model):
    elevator = models.ForeignKey(Elevator, on_delete=models.CASCADE)
    floor = models.IntegerField()
    direction = models.CharField(max_length=10)