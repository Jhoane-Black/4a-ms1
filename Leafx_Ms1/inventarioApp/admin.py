from django.contrib import admin
from .models import Proveedor, Producto, Cliente, Comentario

# Register your models here.

admin.site.register(Proveedor)
admin.site.register(Producto)
admin.site.register(Cliente)
admin.site.register(Comentario)

