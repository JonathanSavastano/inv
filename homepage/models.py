from django.db import models

# Create your models here.
class Computer(models.Model):
    name = models.CharField(max_length=200, unique=True)
    serial_number = models.CharField(max_length=100, unique=True)
    brand = models.CharField(max_length=200)
    model = models.CharField(max_length=200)

    def __str__(self):
        return self.name