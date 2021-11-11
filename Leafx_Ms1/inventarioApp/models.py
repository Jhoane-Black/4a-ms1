from django.db import models

# Create your models here.

class Proveedor(models.Model):
    nombre = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)
    nit = models.BigIntegerField(default=0) 
    email = models.EmailField()
    def __str__(self):
        return self.nombre
    


class Producto(models.Model): 
    nombre = models.CharField(max_length=50)
    precio = models.IntegerField()
    stock  = models.IntegerField()
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE, null=True)
    def __str__(self):
        return self.nombre



class Cliente(models.Model):
    nombre = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)
    email = models.EmailField()
    def __str__(self):
        return self.nombre



class Comentario(models.Model):
    CHOICES = (
        ('0', 'Sin estrellas'),
        ('1', 'Una estrella'),
        ('2', 'Dos estrellas'),
        ('3', 'Tres estrellas'),
        ('4', 'Cuatro estrellas'),
        ('5', 'Cinco estrellas'),
    ) 
    producto = models.ForeignKey(Producto, on_delete=models.SET_NULL, null=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.SET_NULL, null=True)
    calificacion = models.CharField(max_length=1, choices = CHOICES)
    comentario = models.TextField(blank=True)
    creacion   = models.DateField(auto_now_add = True)
    def __str__(self):
        return str(self.cliente) + ": " + str(self.comentario)