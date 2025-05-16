#15/04/2025 VRBAT - # business funkce a logika implementovat zde
from .models import DeliveryHeader
from .models import Customers
from .models import DeliveryItem

import requests #libka http requesty
from datetime import datetime 

# Třída hlavička dodávky - filtr
class DeliveryHeaderFilterService: 
    def __init__(self, request):
        self.request = request #bere vsechny html filtry s parametrem get
        self.queryset = DeliveryHeader.objects.all() 

    def apply_filters(self):
        filters = {
            'delivery_number': 'icontains', #icontains = lookup výraz (filtr), vyhledávání záznamů v db
            'delivery_type': 'icontains',
            'invoice_number': 'icontains',
            'invoice_currency': 'iexact',
            'customer_code': 'icontains',
            'delivery_created_by': 'icontains',
        }
        
        for field, lookup in filters.items():
            value = self.request.GET.get(field)
            if value:
                self.queryset = self.queryset.filter(**{f"{field}__{lookup}": value}) #**kwargs = přejme vše do slovníku
        
        return self.queryset

# Třída zákazník - filtr
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

# Třída položka dodávky - filtr
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
    
#Třída měna
class Mena:
    CURRENCY_API_URL = "https://www.cnb.cz/cs/financni-trhy/devizovy-trh/kurzy-devizoveho-trhu/kurzy-devizoveho-trhu/denni_kurz.txt"

    def __init__(self, target_currency='CZK'):
        self.target_currency = target_currency
        self.currency_rates = self.fetch_currency_rates()

    def fetch_currency_rates(self):
        today_date = datetime.today().strftime('%d.%m.%Y')
        response = requests.get(f"{self.CURRENCY_API_URL}?date={today_date}")

        if response.status_code != 200:
            raise ValueError("Nepodařilo se stáhnout kurzy měn")

        return self.parse_exchange_rates(response.text)

    def parse_exchange_rates(self, data):
        rates = {'CZK': 1.0}
        lines = data.splitlines()
        for line in lines:
            parts = line.split('|')
            if len(parts) > 4:
                currency = parts[3].strip()
                try:
                    rate = float(parts[4].replace(',', '.'))
                    rates[currency] = rate
                except ValueError:
                    continue
        return rates

    def get_rate(self, currency):
        return self.currency_rates.get(currency, None)

    def convert(self, amount, from_currency, to_currency):
        if from_currency == to_currency:
            return round(amount, 2)

        from_rate = self.get_rate(from_currency)
        to_rate = self.get_rate(to_currency)

        if from_rate is None or to_rate is None:
            raise ValueError(f"Neznámý kurz pro měnu {from_currency} nebo {to_currency}")

        amount_in_czk = amount * from_rate
        converted_amount = amount_in_czk / to_rate
        return round(converted_amount, 2)

#Třída DPH dle měny
class DPH:
    def __init__(self, currency):
        self.currency = currency

    def get_vat_rate(self):
        return 0.21

# Třída zákazník 
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

#Třída položka dodávky - zpracování
class DeliveryItemProcessor:
    def __init__(self, items, vat_rate, converter: Mena):
        self.items = items
        self.vat_rate = vat_rate
        self.converter = converter

    def process_items(self):
        processed = []

        for item in self.items:
            total_price = float(item.price_unit_no_dph) * item.delivered_qty
            total_price_vat = total_price * (1 + self.vat_rate)

            converted_price = self.converter.convert(total_price, item.price_unit_currency, self.converter.target_currency)
            converted_price_vat = self.converter.convert(total_price_vat, item.price_unit_currency, self.converter.target_currency)

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

# Třída dodávka - kompletace
class DeliveryService:
    def __init__(self, delivery_header: DeliveryHeader):
        self.delivery_header = delivery_header
        self.converter = Mena(delivery_header.invoice_currency)
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
            "summary": self.calculate_summary(processed_items),
            "exchange_rate": self.converter.get_rate(self.delivery_header.invoice_currency),
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