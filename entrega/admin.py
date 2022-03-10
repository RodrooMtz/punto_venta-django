from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Entrega
# Register your models here.


class EntregaAdmin(admin.ModelAdmin):
    list_display = ('name_producto', 'cantidad', 'precio', 'estado', 'proveedor')


admin.site.register(Entrega, EntregaAdmin)