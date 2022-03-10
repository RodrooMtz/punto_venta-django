from django.db import models


# Create your models here.
class Proveedor(models.Model):
    nombre_proveedor = models.CharField(max_length=50, unique=True)
    descripcion = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.nombre_proveedor
