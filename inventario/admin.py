from django.contrib import admin
from .models import Inventario

# Register your models here.


class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre_categoria', 'descripcion')


admin.site.register(Inventario)
