from django.db import models

# Create your models here.
class Clientes(models.Model):
    nombre = models.CharField(max_length=32)
    direccion = models.CharField(max_length=50)
    email = models.EmailField()
    telefono = models.CharField(max_length=15)

class Articulos(models.Model):
    nombre = models.CharField(max_length=32)
    seccion = models.CharField(max_length=20)
    precio = models.IntegerField()

class Pedidos(models.Model):
    numero_pedido = models.IntegerField()
    fecha = models.DateField()
    entregado = models.BooleanField()