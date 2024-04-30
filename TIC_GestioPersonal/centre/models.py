from django.db import models


# Create your models here.
class Rol(models.Model):
    nom = models.CharField(max_length=255)

    def __str__(self):
        return self.nom

    class Meta:
        app_label = "centre"


class Assignatura(models.Model):
    assignatures = models.CharField(max_length=255)

    def __str__(self):
        return self.assignatures

    class Meta:
        app_label = "centre"


class Usuari(models.Model):
    nom = models.CharField(max_length=255)
    cognom = models.CharField(max_length=255)
    assignatures = models.ForeignKey(Assignatura, on_delete=models.CASCADE)
    rol = models.ForeignKey(Rol, on_delete=models.CASCADE)

    class Meta:
        app_label = "centre"
