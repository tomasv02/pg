from django.contrib import admin

# Register your models here.

#14.04.2025 VRBAT - databáze - vytvoření admin rozhraní
from import_export.admin import ImportExportModelAdmin
from .models import DeliveryItem
from .models import DeliveryHeader
from .models import Customers

#admin.site.register(delivery)

#14.04.2025 VRBAT - tabulka delivery items
@admin.register(DeliveryItem)
class delivery_itemsAdmin(ImportExportModelAdmin):
    pass

#15.04.2025 VRBAT - tabulka delivery header
@admin.register(DeliveryHeader)
class delivery_itemsAdmin(ImportExportModelAdmin):
    pass

#15.04.2025 VRBAT - tabulka customers
@admin.register(Customers)
class customersAdmin(ImportExportModelAdmin):
    pass
