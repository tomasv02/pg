from django.shortcuts import render

from django.views.generic import ListView
from .models import DeliveryHeader

# Create your views here
class DeliveryHeaderListView(ListView):
    model = DeliveryHeader
    template_name = 'print.html'  # jméno šablony
    context_object_name = 'headers'  # proměnná použitá v šabloně