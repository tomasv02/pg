from django.contrib import admin

# Register your models here.

#14.04.2025 VRBAT - databáze - vytvoření admin rozhraní
from django.contrib import admin
from .models import delivery

admin.site.register(delivery)