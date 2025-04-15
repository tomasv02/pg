from django.shortcuts import render
from django.views.generic import ListView
from .models import DeliveryHeader
from .models import Customers
from .models import DeliveryItem

from django.views import View
from django.http import HttpResponse
from django.template.loader import get_template
import weasyprint


#třída dodávky - hlavička  
class DeliveryHeaderListView(ListView):
    model = DeliveryHeader
    template_name = 'print.html'  # jméno šablony
    context_object_name = 'headers'  # proměnná použitá v šabloně

    def get_queryset(self):
        queryset = DeliveryHeader.objects.all()

        # Filtry podle hodnot z GET requestu
        delivery_number = self.request.GET.get('delivery_number')
        delivery_type = self.request.GET.get('delivery_type')
        invoice_number = self.request.GET.get('invoice_number')
        invoice_currency = self.request.GET.get('invoice_currency')
        customer_code = self.request.GET.get('customer_code')
        delivery_created_by = self.request.GET.get('delivery_created_by')

        if delivery_number:
            queryset = queryset.filter(delivery_number__icontains=delivery_number)
        if delivery_type:
            queryset = queryset.filter(delivery_type__icontains=delivery_type)
        if invoice_number:
            queryset = queryset.filter(invoice_number__icontains=invoice_number)
        if invoice_currency:
            queryset = queryset.filter(invoice_currency__iexact=invoice_currency)
        if customer_code:
            queryset = queryset.filter(customer_code__icontains=customer_code)
        if delivery_created_by:
            queryset = queryset.filter(delivery_created_by__icontains=delivery_created_by)

        return queryset

#třída zákazníci    
class CustomersListView(ListView):
    model = Customers
    template_name = 'report_customers.html'  # Jméno šablony
    context_object_name = 'customers'  # Proměnná použitá v šabloně

    def get_queryset(self):
        queryset = Customers.objects.all()

        # Filtry podle hodnot z GET requestu
        customer_code = self.request.GET.get('customer_code')
        customer_text = self.request.GET.get('customer_text')
        customer_city = self.request.GET.get('customer_city')

        if customer_code:
            queryset = queryset.filter(customer_code__icontains=customer_code)
        if customer_text:
            queryset = queryset.filter(customer_text__icontains=customer_text)
        if customer_city:
            queryset = queryset.filter(customer_city__icontains=customer_city)

        return queryset

#třída dodávky - položky     
class DeliveryItemListView(ListView):
    model = DeliveryItem
    template_name = 'report_items.html'  # Šablona, která bude použita
    context_object_name = 'items'  # Název proměnné, která bude obsahovat seznam položek
    
    def get_queryset(self):
        queryset = DeliveryItem.objects.all()

        # Filtry podle hodnot z GET requestu pro všechna pole
        delivery_number = self.request.GET.get('delivery_number')
        delivery_item = self.request.GET.get('delivery_item')
        material = self.request.GET.get('material')
        material_text = self.request.GET.get('material_text')
        delivered_qty = self.request.GET.get('delivered_qty')
        delivered_qty_unit = self.request.GET.get('delivered_qty_unit')
        price_unit_no_dph = self.request.GET.get('price_unit_no_dph')
        price_unit_currency = self.request.GET.get('price_unit_currency')
        delivery_item_created_on = self.request.GET.get('delivery_item_created_on')
        delivery_item_created_at = self.request.GET.get('delivery_item_created_at')
        delivery_item_created_by = self.request.GET.get('delivery_item_created_by')

        # Aplikování filtrů podle GET parametrů
        if delivery_number:
            queryset = queryset.filter(delivery_number__icontains=delivery_number)
        if delivery_item:
            queryset = queryset.filter(delivery_item__icontains=delivery_item)
        if material:
            queryset = queryset.filter(material__icontains=material)
        if material_text:
            queryset = queryset.filter(material_text__icontains=material_text)
        if delivered_qty:
            queryset = queryset.filter(delivered_qty__icontains=delivered_qty)
        if price_unit_no_dph:
            queryset = queryset.filter(price_unit_no_dph__icontains=price_unit_no_dph)
        if delivery_item_created_on:
            queryset = queryset.filter(delivery_item_created_on__icontains=delivery_item_created_on)
        if delivery_item_created_at:
            queryset = queryset.filter(delivery_item_created_at__icontains=delivery_item_created_at)
        if delivery_item_created_by:
            queryset = queryset.filter(delivery_item_created_by__icontains=delivery_item_created_by)

        return queryset
