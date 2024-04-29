from django.db import models

# Create your models here.

class Person(models.Model):
    nom = models.CharField(max_length=255)
    cognom = models.CharField(max_length=255)
    assignatures = models.CharField(max_length=255)
    rol = models.CharField(max_length=255)
    class Meta:
        app_label = 'centre'
