#15/04/2025 VRBAT - # business funkce a logika zde
from .models import DeliveryHeader
from .models import Customers
from .models import DeliveryItem

#třídy: filtry na HTML views - logika
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
    
#logika dopočty do PDF exportu faktury (DPH, konečné součty atp.)
from decimal import Decimal
from .models import DeliveryHeader, DeliveryItem, Customers

class DeliveryItemService:
    def __init__(self, item: DeliveryItem):
        self.item = item

    @property
    def total_no_dph(self):
        return self.item.price_unit_no_dph * self.item.delivered_qty

    @property
    def dph(self):
        return self.total_no_dph * Decimal("0.21")

    @property
    def total_with_dph(self):
        return self.total_no_dph + self.dph


class DeliveryService:
    def __init__(self, delivery):
        self.delivery = delivery
        self.items = DeliveryItem.objects.filter(delivery_number=delivery.delivery_number)
        self.customer = Customers.objects.filter(customer_code=delivery.customer_code).first()

    def get_items_data(self):
        result = []
        for item in self.items:
            item_service = DeliveryItemService(item)
            result.append({
                "material": item.material,
                "text": item.material_text,
                "qty": item.delivered_qty,
                "unit": item.delivered_qty_unit,
                "price_unit": item.price_unit_no_dph,
                "total_no_dph": item_service.total_no_dph,
                "dph": item_service.dph,
                "total_with_dph": item_service.total_with_dph,
            })
        return result

    @property
    def total_no_dph(self):
        return sum(DeliveryItemService(item).total_no_dph for item in self.items)

    @property
    def total_dph(self):
        return sum(DeliveryItemService(item).dph for item in self.items)

    @property
    def total_with_dph(self):
        return sum(DeliveryItemService(item).total_with_dph for item in self.items)

    def as_dict(self):
        return {
            "header": self.delivery,  # Zde máme DeliveryHeader
            "customer": self.customer,
            "items": self.get_items_data(),
            "total_no_dph": self.total_no_dph,
            "total_dph": self.total_dph,
            "total_with_dph": self.total_with_dph
        }