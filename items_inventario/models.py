from django.db import models
from inventario.models import Inventario
# Create your models here.


class Producto(models.Model):
    nombre_producto = models.CharField(max_length=200, unique=True)
    descripcion = models.TextField(max_length=500, blank=True)
    precio = models.IntegerField()
    images = models.ImageField(upload_to='photos/products')
    stock = models.IntegerField()
    disponible = models.BooleanField(default=True)
    categoria = models.ForeignKey(Inventario, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre_producto


