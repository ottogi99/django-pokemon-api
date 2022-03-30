from django.db import models

# Create your models here.
from django.db import models


class IllustratedGuide(models.Model):
    id = models.BigAutoField(primary_key=True)
    number = models.CharField(max_length=10)
    name = models.CharField(max_length=20)
    monType = models.CharField(max_length=20)
    height = models.CharField(max_length=10, blank=True, null=True)
    weight = models.CharField(max_length=10, blank=True, null=True)
    thumbnail = models.CharField(max_length=256)
    fullImage = models.CharField(max_length=256, blank=True, null=True)
