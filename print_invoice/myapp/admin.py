from django.contrib import admin

# Register your models here.

#14.04.2025 VRBAT - databáze - vytvoření admin rozhraní
from import_export.admin import ImportExportModelAdmin
from .models import delivery_item
from .models import delivery_header

#admin.site.register(delivery)

#14.04.2025 VRBAT - databáze deliveries - features: nahrávání dat z excelu přes admin rozhraní
@admin.register(delivery_item)
class delivery_itemsAdmin(ImportExportModelAdmin):
    pass

@admin.register(delivery_header)
class delivery_itemsAdmin(ImportExportModelAdmin):
    pass