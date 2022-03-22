from django.contrib import admin
from cuenta.models import Sale


class SaleAdmin(admin.ModelAdmin):
    list_display = ('date_joined', 'iva', 'numero_mesa')


admin.site.register(Sale, SaleAdmin)

