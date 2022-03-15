from django.contrib import admin

from general.models import General


class GeneralAdmin(admin.ModelAdmin):
    list_display = ('date_joined', 'ingreso_efectivo', 'ingreso_tarjeta', 'numero_mesas', 'propina_tarjeta')


admin.site.register(General, GeneralAdmin)
