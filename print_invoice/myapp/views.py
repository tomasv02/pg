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

#13/04/2025 VRBAT - view webové aplikace
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
#13/05/2025 VRBAT - dekorátor = vypnutí CSRF ochrany, není potřeba token pro metodu POST 
# pouze na dev. sys, nikdy ne do produkce!!! - vyhodí to Forbidden (403) 

def export_selected_deliveries(request):
    if request.method == "POST":
        selected_id = request.POST.get('selected_id')  # výběr z radio buttonu v html
        if not selected_id:
            return HttpResponse("Nebyla vybrána žádná dodávka.", status=400)

        # Získání dodávky podle ID
        delivery = DeliveryHeader.objects.filter(id=selected_id).first()
        if not delivery:
            return HttpResponse("Dodávka nebyla nalezena.", status=404)

        delivery_service = DeliveryService(delivery)
        enriched_delivery = delivery_service.as_dict()

        #generování HTML šablony
        try:
            html_string = render_to_string("export_pdf.html", {
                'deliveries': [enriched_delivery]  # list kvůli šabloně
            })
        except Exception as e:
            return HttpResponse(f"Chyba při generování HTML: {e}", status=500)

        # Absolutní cesta k CSS souboru - jinak to prostě nejde
        css_path = os.path.join(settings.BASE_DIR, 'print_invoice', 'static', 'css', 'pdf-style.css')

        # generování PDF
        try:
            html = HTML(string=html_string)
            css = CSS(filename=css_path)

            response = HttpResponse(content_type='application/pdf')
            response['Content-Disposition'] = f'inline; filename="faktura_{enriched_delivery["header"].invoice_number}.pdf"'
            
            html.write_pdf(target=response, stylesheets=[css])
        except Exception as e:
            return HttpResponse(f"Chyba při generování PDF: {e}", status=500)

        return response
    else:
        return HttpResponse("Metoda není povolena", status=405)
    
    