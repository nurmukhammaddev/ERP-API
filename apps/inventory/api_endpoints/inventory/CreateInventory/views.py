from rest_framework import generics

from apps.inventory.models import Inventory

from .serializers import InventorySerializer


class InventoryCreateApiView(generics.ListCreateAPIView):
    serializer_class = InventorySerializer
    queryset = Inventory.objects.all()


__all__ = ["InventoryCreateApiView"]
