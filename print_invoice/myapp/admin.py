from django.contrib import admin

# Register your models here.

#14.04.2025 VRBAT - databáze - vytvoření admin rozhraní
from import_export.admin import ImportExportModelAdmin
from .models import delivery_item
from .models import delivery_header
from .models import customers

#admin.site.register(delivery)

#14.04.2025 VRBAT - tabulka delivery items
@admin.register(delivery_item)
class delivery_itemsAdmin(ImportExportModelAdmin):
    pass

#15.04.2025 VRBAT - tabulka delivery header
@admin.register(delivery_header)
class delivery_itemsAdmin(ImportExportModelAdmin):
    pass

#15.04.2025 VRBAT - tabulka customers
@admin.register(customers)
class customersAdmin(ImportExportModelAdmin):
    pass