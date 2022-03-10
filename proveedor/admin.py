from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Proveedor

# Register your models here.


class ProveedorAdmin(admin.ModelAdmin):
    list_display = ('nombre_proveedor', 'descripcion')


admin.site.register(Proveedor, ProveedorAdmin)