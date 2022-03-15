from django.contrib import admin

from promocion.models import Promocion, ProductosDias


class promocioInline(admin.TabularInline):
    model = ProductosDias
    extra = 1
    autocomplete_fields = ['producto1']


class PromocionAdmin(admin.ModelAdmin):
    inlines = [promocioInline, ]
    list_display = ('nombre_promocion', 'imagen')


class Producto1Admin(admin.ModelAdmin):
    inlines = (promocioInline,)
    search_fields = 'producto1',
    ordering = ['producto1']


admin.site.register(Promocion, PromocionAdmin)
admin.site.register(ProductosDias)


