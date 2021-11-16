from rest_framework import generics
from ..models import Proveedor, Producto, Cliente, Comentario
from ..serializers import ProductoSerializer, ComentarioSerializer

# Resumen

class ComentariosDeProductoList(generics.ListAPIView):
    serializer_class = ComentarioSerializer

    def get(self, request, *args, **kwargs):
        producto = Producto.objects.get(pk=kwargs['pk'])
        self.queryset = Comentario.objects.filter(producto=producto).order_by("-creacion",'-calificacion')
        return self.list(request, *args, **kwargs)


class ComentariosDeClienteList(generics.ListAPIView):
    serializer_class = ComentarioSerializer

    def get(self, request, *args, **kwargs):
        cliente = Cliente.objects.get(pk=kwargs['pk'])
        self.queryset = Comentario.objects.filter(cliente=cliente).order_by("-creacion", '-calificacion')
        return self.list(request, *args, **kwargs)


class ProductosDeProveedorList(generics.ListAPIView):
    serializer_class = ProductoSerializer

    def get(self, request, *args, **kwargs):
        proveedor = Proveedor.objects.get(pk=kwargs['pk'])
        self.queryset = Producto.objects.filter(proveedor=proveedor).order_by('nombre')
        return self.list(request, *args, **kwargs)