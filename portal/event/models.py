from django.db import models
from django.contrib.auth.models import User



class Event(models.Model):
    name = models.CharField(max_length=50)
    discription = models.CharField(max_length=150)
    time = models.DateTimeField()
    date = models.DateField()
