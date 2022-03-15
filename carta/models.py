from django.db import models
from inventario.models import Inventario


class ProductoMenu(models.Model):
    nombre_platillo = models.CharField(max_length=200, unique=True)
    precio = models.IntegerField()
    images = models.ImageField(upload_to='photos/menu')
    categoria = models.ForeignKey(Inventario, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre_platillo
