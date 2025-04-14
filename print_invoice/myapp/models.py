from django.db import models

# Create your models here.

#14.04.2025 VRBAT - databáze 
#Vždy po úpravě dělej: 
# python manage.py makemigrations myapp - vytvoření migrace
# python manage.py migrate - migrování dat

from django.db import models

class delivery(models.Model):
    delivery_number = models.CharField(max_length=50)  # Např. číslo dodávky
    delivery_item = models.CharField(max_length=200)  # Popis položky
    material = models.CharField(max_length=5)  # Materiál
    material_text = models.CharField(max_length=40)  # Textová poznámka k materiálu
    delivered_qty = models.DecimalField(max_digits=4, decimal_places=0)  # Množství dodané
    delivered_qty_unit = models.CharField(max_length=2, default="KS")  # Jednotka množství
    price_unit_no_dph = models.DecimalField(max_digits=10, decimal_places=2)  # Cena bez DPH
    price_unit_currency = models.CharField(max_length=10)  # Měna ceny
    delivery_item_created_on = models.DateField()  # Datum vytvoření položky
    delivery_item_created_at = models.DateTimeField()  # Čas vytvoření položky
    delivery_item_created_by = models.CharField(max_length=12)  # Kdo položku vytvořil

    def __str__(self):
        return f"Delivery {self.delivery_number} - {self.delivery_item}"