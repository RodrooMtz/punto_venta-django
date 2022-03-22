from django.contrib import admin

# Register your models here.
from carta.models import ProductoMenu


class ProductoMenuAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre_platillo', 'precio', 'categoria')
    search_fields = 'nombre_platillo',


admin.site.register(ProductoMenu, ProductoMenuAdmin)
