from datetime import datetime
from django.forms import ModelForm, TextInput, DateInput
# from entrega.models import Entrega
# from proveedor.models import Proveedor
from .models import Inventario
from cuenta.models import Sale
from carta.models import ProductoMenu


class CategoriaForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nombre_categoria'].widget.attrs['autofocus'] = True

    class Meta:
        model = Inventario
        fields = '__all__'
        widgets = {
            'nombre_categoria': TextInput(
                attrs={
                    'placeholder': 'Ingrese un nombre',
                }
            ),
            'descripcion': TextInput(
                attrs={
                    'placeholder': 'Ingrese una descripción'
                }
            )
        }


class SaleForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['class'] = 'form-control'
            form.field.widget.attrs['autocomplete'] = 'off'
        self.fields['cliente'].widget.attrs['autofocus'] = True

    class Meta:
        model = Sale
        fields = '__all__'
        widgets = {
            'date_joined': DateInput(format='%Y-%m-%d',
                                     attrs={
                                         'value': datetime.now().strftime('%Y-%m-%d')
                                     }
                                     ),
        }


class CartaForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['class'] = 'form-control'
            form.field.widget.attrs['autocomplete'] = 'off'
        self.fields['nombre_platillo'].widget.attrs['autofocus'] = True

    class Meta:
        model = ProductoMenu
        fields = '__all__'
        widgets = {
            'date_joined': DateInput(format='%Y-%m-%d',
                                     attrs={
                                         'value': datetime.now().strftime('%Y-%m-%d')
                                     }
                                     ),
        }
