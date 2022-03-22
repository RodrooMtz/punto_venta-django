from django.db import models

from carta.models import ProductoMenu


class Promocion(models.Model):
    UNO = 'Lunes'
    DOS = 'Martes'
    TRES = 'Miércoles'
    CUATRO = 'Jueves'
    CINCO = 'Viernes'
    SEIS = 'Sábado'
    SIETE = 'Domingo'
    DAYS = (
        (UNO, 'Lunes'),
        (DOS, 'Martes'),
        (TRES, 'Miércoles'),
        (CUATRO, 'Jueves'),
        (CINCO, 'Viernes'),
        (SEIS, 'Sábado'),
        (SIETE, 'Domingo'),
    )
    nombre_promocion = models.CharField(max_length=200, unique=True)
    imagen = models.ImageField(upload_to='photos/promo', blank=True)
    precio = models.IntegerField(blank=True, default=0)
    dia = models.CharField(max_length=10, choices=DAYS, default='')
    producto = models.ManyToManyField(ProductoMenu, through='ProductosDias', through_fields=('promocion1', 'producto1'),
                                      blank=True)

    def __str__(self):
        return self.nombre_promocion


class ProductosDias(models.Model):
    promocion1 = models.ForeignKey(Promocion, on_delete=models.CASCADE, blank=True)
    producto1 = models.ForeignKey(ProductoMenu, on_delete=models.CASCADE, blank=True)

