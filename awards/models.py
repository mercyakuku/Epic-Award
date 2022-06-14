from django.db import models
from django.contrib.auth.models import User
import math

# Create your models here.
class Location(models.Model):
    country = models.CharField(max_length=50, null=True)
    state = models.CharField(max_length=50, null=True)
    zipcode = models.IntegerField(null=True)
    address = models.IntegerField(null=True)

    def __str__(self):
        return self.country
