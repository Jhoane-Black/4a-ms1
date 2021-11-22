from rest_framework import generics
from ..models import Comentario
from ..serializers import ComentarioSerializer

# Comentarios

class ComentarioListCreate(generics.ListCreateAPIView):
    queryset = Comentario.objects.all()
    serializer_class = ComentarioSerializer

class ComentarioUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comentario.objects.all()
    serializer_class = ComentarioSerializer  