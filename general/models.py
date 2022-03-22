from django.db import models
from datetime import datetime


class General(models.Model):
    efectivo_caja = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    date_joined = models.DateField(default=datetime.now)
    ingreso_efectivo = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    ingreso_tarjeta = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    numero_mesas = models.IntegerField(default=0)
    propina_tarjeta = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)

    def __str__(self):
        return str(self.efectivo_caja)
