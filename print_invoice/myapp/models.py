from django.db import models

# Create your models here.

#14.04.2025 VRBAT - databáze 
#Vždy po úpravě dělej: 
# python manage.py makemigrations - vytvoření migrace
# python manage.py migrate - migrování dat

from django.db import models

class delivery_item(models.Model):
    delivery_number = models.CharField(max_length=20)  # Např. číslo dodávky
    delivery_item = models.CharField(max_length=4)  # Popis položky
    material = models.CharField(max_length=5)  # Materiál
    material_text = models.CharField(max_length=40)  # Textová poznámka k materiálu
    delivered_qty = models.IntegerField()  # Množství dodané
    delivered_qty_unit = models.CharField(max_length=2, default="KS")  # Jednotka množství
    price_unit_no_dph = models.DecimalField(max_digits=10, decimal_places=3, default=0)  # Cena bez DPH
    price_unit_currency = models.CharField(max_length=10, default="CZK")  # Měna ceny
    delivery_item_created_on = models.CharField(max_length=20)  # Datum vytvoření položky
    delivery_item_created_at = models.CharField(max_length=20)  # Čas vytvoření položky
    delivery_item_created_by = models.CharField(max_length=12)  # Kdo položku vytvořil

    def __str__(self):
        return f"Delivery {self.delivery_number} - {self.delivery_item}"
    
class delivery_header(models.Model):
    delivery_number = models.CharField(max_length=20, unique=True)
    delivery_type = models.CharField(max_length=2)
    invoice_number = models.CharField(max_length=20, blank=True, null=True)
    invoice_currency = models.CharField(max_length=20)
    due_date_invoice = models.CharField(max_length=20)
    customer = models.CharField(max_length=30)
    delivery_date = models.CharField(max_length=20)
    delivery_created_on = models.CharField(max_length=20)
    delivery_created_at = models.CharField(max_length=20)
    delivery_created_by = models.CharField(max_length=12)

    def __str__(self):
        return f"{self.delivery_number} – {self.customer}"    