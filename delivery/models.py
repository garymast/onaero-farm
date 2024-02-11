from django.db import models

class Suburb(models.Model):

    suburb = models.CharField(max_length=254)
    description = models.TextField(null=True, blank=True)
    population = models.PositiveIntegerField(null=True, blank=True)
    coords = models.CharField(max_length=254)

    def __str__(self):
        return self.suburb

    def get_pop(self):
        if self.population:
            return self.population
        else:
            return "Unknown"
        

