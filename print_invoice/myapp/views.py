from django.shortcuts import render
from django.views.generic import ListView
from .models import DeliveryHeader, Customers, DeliveryItem
from .services import DeliveryHeaderFilterService, CustomersFilterService, DeliveryItemFilterService
from django.views.decorators.csrf import csrf_exempt  
#export do PDF
from django.template.loader import render_to_string
from weasyprint import HTML
from django.http import HttpResponse
from .services import DeliveryService 


class DeliveryHeaderListView(ListView):
    model = DeliveryHeader
    template_name = 'print.html'
    context_object_name = 'headers'

    def get_queryset(self):
        filter_service = DeliveryHeaderFilterService(self.request)
        return filter_service.apply_filters()

class CustomersListView(ListView):
    model = Customers
    template_name = 'report_customers.html'
    context_object_name = 'customers'

    def get_queryset(self):
        filter_service = CustomersFilterService(self.request)
        return filter_service.apply_filters()

class DeliveryItemListView(ListView):
    model = DeliveryItem
    template_name = 'report_items.html'
    context_object_name = 'items'

    def get_queryset(self):
        filter_service = DeliveryItemFilterService(self.request)
        return filter_service.apply_filters()


#výstup pro export do PDF
@csrf_exempt
def export_selected_deliveries(request):
    if request.method == "POST":
        ids = request.POST.getlist('selected_ids')
        deliveries = DeliveryHeader.objects.filter(id__in=ids)

        enriched_deliveries = []
        for delivery in deliveries:
            delivery_service = DeliveryService(delivery)
            enriched_deliveries.append(delivery_service.as_dict())

        html_string = render_to_string("export_pdf.html", {
            'deliveries': enriched_deliveries
        })

        html = HTML(string=html_string)
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = f'inline; filename="faktura_{enriched_deliveries[0]["header"].invoice_number}.pdf"'
        html.write_pdf(target=response)
        return response