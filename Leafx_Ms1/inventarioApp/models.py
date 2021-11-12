from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Proveedor(models.Model):
    nombre = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)
    nit = models.PositiveIntegerField(default=0) 
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    def __str__(self):
        return self.nombre
    


class Producto(models.Model): 
    nombre = models.CharField(max_length=50)
    precio = models.PositiveIntegerField(default=0)
    stock  = models.PositiveIntegerField(default=0)
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    def __str__(self):
        return self.nombre



class Cliente(models.Model):
    nombre = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    def __str__(self):
        return self.nombre



class Comentario(models.Model):
    CHOICES = (
        (0, '  '),
        (1, '★'),
        (2, '★ ★'),
        (3, '★ ★ ★'),
        (4, '★ ★ ★ ★'),
        (5, '★ ★ ★ ★ ★'),
    ) 
    producto = models.ForeignKey(Producto, on_delete=models.SET_NULL, null=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.SET_NULL, null=True)
    calificacion = models.IntegerField(default=0, choices = CHOICES)
    comentario = models.TextField(blank=True)
    creacion   = models.DateField(auto_now_add = True)
    def __str__(self):
        return str(self.cliente) + ": " + str(self.comentario)