from user.models import User
from django.db import models
from datetime import datetime

from carta.models import ProductoMenu
from general.models import General


class Sale(models.Model):
    STATUS = (
        ('Pagado', 'Pagado'),
        ('En espera', 'En espera'),
    )
    cliente = models.CharField(max_length=255, blank=True, unique=True)
    date_joined = models.DateField(default=datetime.now)
    subtotal = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    iva = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    total = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    efectivo_caja = models.ForeignKey(General, on_delete=models.CASCADE)
    efectivo = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    tarjeta = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    numero_mesa = models.IntegerField(blank=False, default=0)
    mesero = models.ForeignKey(User, on_delete=models.CASCADE, default='')
    estado = models.CharField(max_length=10, choices=STATUS, default='')
    producto = models.ForeignKey(ProductoMenu, on_delete=models.CASCADE, default='')
    comentarios = models.CharField(max_length=255, blank=True, default='')

    def __str__(self):
        return self.cliente
