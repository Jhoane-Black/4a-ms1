from rest_framework import generics
from ..models import Proveedor
from ..serializers import ProveedorSerializer

# Proveedor

class ProveedorListCreate(generics.ListCreateAPIView):
    queryset = Proveedor.objects.all()
    serializer_class = ProveedorSerializer

class ProveedorUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Proveedor.objects.all()
    serializer_class = ProveedorSerializer