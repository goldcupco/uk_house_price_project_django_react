# house_price_analysis/models.py

from django.db import models

class HousePrice(models.Model):
    date = models.DateField()
    average_price = models.DecimalField(max_digits=10, decimal_places=2)
    detached_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    semi_detached_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    terraced_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    flat_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return f"House Price on {self.date}"

class Region(models.Model):
    name = models.CharField(max_length=100)
    average_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name