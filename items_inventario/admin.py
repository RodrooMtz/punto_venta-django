from django.contrib import admin
from .models import Producto
# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = ('nombre_producto', 'precio', 'stock', 'disponible', 'categoria')


admin.site.register(Producto, ProductAdmin)
