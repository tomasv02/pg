"""
URL configuration for print_invoice project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from . import views #14/04/2025 VRBAT - zavolání html views
from myapp.views import DeliveryHeaderListView
from myapp.views import CustomersListView
from myapp.views import DeliveryItemListView

urlpatterns = [
    path("admin/", admin.site.urls), #pristus do admin modu z homepage
    path('', views.homepage), #domovská stránka
    path('print/', DeliveryHeaderListView.as_view(), name='delivery_header_list'), #15.04.2025 VRBAT - propojení class view a html print
    path('report_customers/', CustomersListView.as_view(), name='customers_list'), #15.04.2025 VRBAT - zákazníci propojení
    path('report_items/', DeliveryItemListView.as_view(), name='delivery_item_list'),  #15.04.2025 VRBAT - Seznam položek dodávky
]
