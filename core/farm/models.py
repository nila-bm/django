from django.db import models

# Create your models here.

class Farm(models.Model):
    name=models.CharField(max_length=50)
    city=models.CharField(max_length=30)
    area=models.DecimalField(max_digits=10,decimal_places=2)

    def __str__(self):
      return self.name
    