from django.db import models

# Create your models here.

#14.04.2025 VRBAT - databáze 
#Vždy po úpravě dělej: 
# python manage.py makemigrations - vytvoření migrace
# python manage.py migrate - migrování dat

from django.db import models

class delivery_item(models.Model):
    delivery_number = models.CharField(max_length=20)  # NEunikátní
    delivery_item = models.CharField(max_length=4)
    material = models.CharField(max_length=5)
    material_text = models.CharField(max_length=40)
    delivered_qty = models.IntegerField()
    delivered_qty_unit = models.CharField(max_length=2, default="KS")
    price_unit_no_dph = models.DecimalField(max_digits=10, decimal_places=3, default=0)
    price_unit_currency = models.CharField(max_length=6, default="CZK")
    delivery_item_created_on = models.CharField(max_length=20)
    delivery_item_created_at = models.CharField(max_length=20)
    delivery_item_created_by = models.CharField(max_length=12)

    def __str__(self):
        return f"Delivery {self.delivery_number} - {self.delivery_item}"


class delivery_header(models.Model):
    delivery_number = models.CharField(max_length=20)
    delivery_type = models.CharField(max_length=2)
    invoice_number = models.IntegerField(default=0)  
    invoice_currency = models.CharField(max_length=6)
    due_date_invoice = models.CharField(max_length=20)
    customer = models.CharField(max_length=30)
    delivery_date = models.CharField(max_length=20)
    delivery_created_on = models.CharField(max_length=20)
    delivery_created_at = models.CharField(max_length=20)
    delivery_created_by = models.CharField(max_length=12)

    def __str__(self):
        return f"{self.delivery_number} – {self.customer}"    

class customers(models.Model):
    customer_code = models.CharField(max_length=5)
    customer_text = models.CharField(max_length=60)  # Název zákazníka nebo popis
    customer_ico = models.CharField(max_length=20)  # IČO
    customer_street = models.CharField(max_length=128)
    customer_cp = models.CharField(max_length=20)  # Číslo popisné
    customer_zip = models.CharField(max_length=10)
    customer_city = models.CharField(max_length=60)
    customer_email = models.CharField(max_length=60)
    customer_phone = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.customer_code} – {self.customer_text}"