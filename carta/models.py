from django.db import models

# Create your models here.
from inventario.models import Inventario


class ProductoMenu(models.Model):
    nombre_platillo = models.CharField(max_length=200, unique=True)
    descripcion = models.TextField(max_length=500, blank=True)
    precio = models.IntegerField()
    images = models.ImageField(upload_to='photos/menu')
    stock = models.IntegerField()
    disponible = models.BooleanField(default=True)
    categoria = models.ForeignKey(Inventario, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre_platillo
