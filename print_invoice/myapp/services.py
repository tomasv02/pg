from .models import DeliveryHeader
from datetime import datetime

#15/04/2025 VRBAT - # filtrování dodávek

class DeliveryService:
    @staticmethod
    def get_all_deliveries():
        return DeliveryHeader.objects.all()