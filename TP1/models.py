from django.db import models

class Voiture(models.Model):
    marque = models.CharField(max_length=100)
    date_achat = models.DateField()
    nombre_places = models.IntegerField()
    description = models.TextField()
    longueur = models.FloatField()
    climatisation = models.BooleanField(default=False)

    def __str__(self):
        return self.marque