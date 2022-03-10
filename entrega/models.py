from django.db import models
from proveedor.models import Proveedor


class Entrega(models.Model):
    name_producto = models.CharField(max_length=200, unique=True)
    cantidad = models.IntegerField()
    precio = models.IntegerField()
    estado = models.BooleanField(default=False)
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)

    def __str__(self):
        return self.name_producto
