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
from .models import Customers, DeliveryItem, DeliveryHeader

CURRENCY_RATES = {
    "EUR": 25.010,
    "USD": 22.024,
    "GBP": 29.138,
    "CZK": 1.0,
}

# Třída pro převod měny
class CurrencyConverter:
    def __init__(self, target_currency):
        self.target_currency = target_currency
        self.rate = CURRENCY_RATES.get(target_currency, 1.0)

    def convert(self, amount):
        return round(amount / self.rate, 2)


#Třída pro výpočet DPH dle měny
class DPH:
    def __init__(self, currency):
        self.currency = currency

    def get_vat_rate(self):
        return 0.21  #sazba pro výpočet DPH


# Data o zákazníkovi
class CustomerInfoBuilder:
    def __init__(self, customer_code):
        self.customer = Customers.objects.filter(customer_code=customer_code).first()

    def build(self):
        c = self.customer
        if not c:
            return {
                "name": "-",
                "ico": "-",
                "address": "-",
                "email": "-",
                "phone": "-",
            }

        return {
            "name": c.customer_text,
            "ico": c.customer_ico,
            "address": f"{c.customer_street} {c.customer_cp}, {c.customer_zip} {c.customer_city}",
            "email": c.customer_email,
            "phone": c.customer_phone,
        }


#Zpracování položek dodávky (DPH, konverze)
class DeliveryItemProcessor:
    def __init__(self, items, vat_rate, converter):
        self.items = items
        self.vat_rate = vat_rate
        self.converter = converter

    def process_items(self):
        processed = []

        for item in self.items:
            total_price = float(item.price_unit_no_dph) * item.delivered_qty
            total_price_vat = total_price * (1 + self.vat_rate)

            converted_price = self.converter.convert(total_price)
            converted_price_vat = self.converter.convert(total_price_vat)

            processed.append({
                "item_number": item.delivery_item,
                "material": item.material,
                "description": item.material_text,
                "quantity": item.delivered_qty,
                "unit": item.delivered_qty_unit,
                "price_per_unit": item.price_unit_no_dph,
                "currency": item.price_unit_currency,
                "total_price": round(total_price, 2),
                "total_price_vat": round(total_price_vat, 2),
                "total_price_converted": converted_price,
                "total_price_vat_converted": converted_price_vat,
                "converted_currency": self.converter.target_currency,
                "created_on": item.delivery_item_created_on,
                "created_at": item.delivery_item_created_at,
                "created_by": item.delivery_item_created_by,
            })

        return processed


# Hlavní služba pro sestavení výstupu pro PDF export
class DeliveryService:
    def __init__(self, delivery_header: DeliveryHeader):
        self.delivery_header = delivery_header
        self.converter = CurrencyConverter(delivery_header.invoice_currency)
        self.vat_rate = DPH(delivery_header.invoice_currency).get_vat_rate()

    def as_dict(self):
        customer_info = CustomerInfoBuilder(self.delivery_header.customer_code).build()
        items = DeliveryItem.objects.filter(delivery_number=self.delivery_header.delivery_number)
        item_processor = DeliveryItemProcessor(items, self.vat_rate, self.converter)

        processed_items = item_processor.process_items()

        return {
            "header": self.delivery_header,
            "customer": customer_info,
            "items": processed_items,
            "summary": self.calculate_summary(processed_items)
        }

    def calculate_summary(self, items):
        total_no_dph = sum(item["total_price"] for item in items)
        total_with_dph = sum(item["total_price_vat"] for item in items)
        total_converted = sum(item["total_price_converted"] for item in items)
        total_converted_with_dph = sum(item["total_price_vat_converted"] for item in items)

        return {
            "total_no_dph": round(total_no_dph, 2),
            "total_with_dph": round(total_with_dph, 2),
            "total_converted": round(total_converted, 2),
            "total_converted_with_dph": round(total_converted_with_dph, 2),
            "currency": self.delivery_header.invoice_currency,
        }

