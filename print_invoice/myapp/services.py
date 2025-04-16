#15/04/2025 VRBAT - # business funkce a logika zde
from .models import DeliveryHeader
from .models import Customers
from .models import DeliveryItem

class DeliveryHeaderFilterService:
    def __init__(self, request):
        self.request = request
        self.queryset = DeliveryHeader.objects.all()

    def apply_filters(self):
        filters = {
            'delivery_number': 'icontains',
            'delivery_type': 'icontains',
            'invoice_number': 'icontains',
            'invoice_currency': 'iexact',
            'customer_code': 'icontains',
            'delivery_created_by': 'icontains',
        }
        
        for field, lookup in filters.items():
            value = self.request.GET.get(field)
            if value:
                self.queryset = self.queryset.filter(**{f"{field}__{lookup}": value})
        
        return self.queryset


class CustomersFilterService:
    def __init__(self, request):
        self.request = request
        self.queryset = Customers.objects.all()

    def apply_filters(self):
        filters = {
            'customer_code': 'icontains',
            'customer_text': 'icontains',
            'customer_city': 'icontains',
        }

        for field, lookup in filters.items():
            value = self.request.GET.get(field)
            if value:
                self.queryset = self.queryset.filter(**{f"{field}__{lookup}": value})

        return self.queryset


class DeliveryItemFilterService:
    def __init__(self, request):
        self.request = request
        self.queryset = DeliveryItem.objects.all()

    def apply_filters(self):
        filters = {
            'delivery_number': 'icontains',
            'delivery_item': 'icontains',
            'material': 'icontains',
            'material_text': 'icontains',
            'delivered_qty': 'icontains',
            'price_unit_no_dph': 'icontains',
            'delivery_item_created_on': 'icontains',
            'delivery_item_created_at': 'icontains',
            'delivery_item_created_by': 'icontains',
        }

        for field, lookup in filters.items():
            value = self.request.GET.get(field)
            if value:
                self.queryset = self.queryset.filter(**{f"{field}__{lookup}": value})

        return self.queryset