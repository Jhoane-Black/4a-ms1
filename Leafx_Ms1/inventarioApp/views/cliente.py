from rest_framework import generics
from ..models import Cliente
from ..serializers import ClienteSerializer

# Cliente

class ClienteListCreate(generics.ListCreateAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class ClienteUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer 