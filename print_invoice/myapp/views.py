from django.shortcuts import render
from django.views.generic import ListView
from .models import DeliveryHeader, Customers, DeliveryItem
from .services import DeliveryHeaderFilterService, CustomersFilterService, DeliveryItemFilterService
from django.views.decorators.csrf import csrf_exempt  
#export do PDF
from django.template.loader import render_to_string
from weasyprint import HTML, CSS
from django.http import HttpResponse
from .services import DeliveryService 
from django.conf import settings
import os


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


# výstup pro export do PDF
@csrf_exempt
def export_selected_deliveries(request):
    if request.method == "POST":
        selected_id = request.POST.get('selected_id')  # výběr z radio buttonu v html
        if not selected_id:
            return HttpResponse("Nebyla vybrána žádná dodávka.", status=400)

        delivery = DeliveryHeader.objects.filter(id=selected_id).first()
        if not delivery:
            return HttpResponse("Dodávka nebyla nalezena.", status=404)

        delivery_service = DeliveryService(delivery)
        enriched_delivery = delivery_service.as_dict()

        html_string = render_to_string("export_pdf.html", {
            'deliveries': [enriched_delivery]  # list kvůli šabloně
        })

        # Absolutní cesta k CSS souboru - tisk faktury do PDF
        css_path = os.path.join(settings.BASE_DIR, 'print_invoice', 'static', 'css', 'pdf-style.css')

        # Vytvoření PDF
        html = HTML(string=html_string)
        css = CSS(filename=css_path)

        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = f'inline; filename="faktura_{enriched_delivery["header"].invoice_number}.pdf"'
        html.write_pdf(target=response, stylesheets=[css])

        return response
    else:
        return HttpResponse("Metoda není povolena", status=405)