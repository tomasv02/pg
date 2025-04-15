from django.shortcuts import render

from django.views.generic import ListView
from .models import DeliveryHeader, Customers

# Create your views here
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
        customer = self.request.GET.get('customer')
        delivery_created_by = self.request.GET.get('delivery_created_by')

        if delivery_number:
            queryset = queryset.filter(delivery_number__icontains=delivery_number)
        if delivery_type:
            queryset = queryset.filter(delivery_type__icontains=delivery_type)
        if invoice_number:
            queryset = queryset.filter(invoice_number__icontains=invoice_number)
        if invoice_currency:
            queryset = queryset.filter(invoice_currency__iexact=invoice_currency)
        if customer:
            queryset = queryset.filter(customer__icontains=customer)
        if delivery_created_by:
            queryset = queryset.filter(delivery_created_by__icontains=delivery_created_by)

        return queryset
    