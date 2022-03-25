from django.db import models
from django.forms import model_to_dict


class Inventario(models.Model):
    nombre_categoria = models.CharField(max_length=50, unique=True)
    descripcion = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.nombre_categoria

    def toJSON(self):
        item = model_to_dict(self)
        return item
