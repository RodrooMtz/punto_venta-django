from datetime import datetime

from user.models import User
from django.forms import ModelForm, TextInput, DateInput, PasswordInput
# from entrega.models import Entrega
# from proveedor.models import Proveedor
from general.models import General
from promocion.models import Promocion, ProductosDias
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
        self.fields['efectivo_caja'].widget.attrs['autofocus'] = True

        self.fields['subtotal'].widget.attrs = {
            'readonly': True,
            'class': 'form-control'
        }

        self.fields['date_joined'].widget.attrs = {
            'readonly': True,
            'class': 'form-control'
        }

        self.fields['total'].widget.attrs = {
            'readonly': True,
            'class': 'form-control'
        }

    class Meta:
        model = Sale
        fields = '__all__'
        widgets = {
            'date_joined': DateInput(
                format='%Y-%m-%d',
                attrs={
                    'value': datetime.now().strftime('%Y-%m-%d')
                }
            ),
            'cliente': TextInput(
                attrs={
                    'placeholder': 'Ingrese el cliente',
                }
            ),
            'iva': TextInput(
                attrs={
                    'readonly': True,
                    'class': 'form-control',
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
            'date_joined': DateInput(
                format='%Y-%m-%d',
                attrs={
                     'value': datetime.now().strftime('%Y-%m-%d')
                }
            ),
        }


class PromocionForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['class'] = 'form-control'
            form.field.widget.attrs['autocomplete'] = 'off'

    class Meta:
        model = ProductosDias
        fields = '__all__'


class Promocion1Form(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['class'] = 'form-control'
            form.field.widget.attrs['autocomplete'] = 'off'
        self.fields['nombre_promocion'].widget.attrs['autofocus'] = True

    class Meta:
        model = Promocion
        fields = '__all__'


class GeneralForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['class'] = 'form-control'
            form.field.widget.attrs['autocomplete'] = 'off'
        self.fields['date_joined'].widget.attrs['autofocus'] = True

    class Meta:
        model = General
        fields = ('efectivo_caja', 'ingreso_tarjeta', 'numero_mesas', 'propina_tarjeta', 'date_joined')
        widgets = {
            'date_joined': DateInput(
                format='%Y-%m-%d',
                attrs={
                    'value': datetime.now().strftime('%Y-%m-%d')
                }
            ),
        }


class UserForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['class'] = 'form-control'
            form.field.widget.attrs['autocomplete'] = 'off'

    class Meta:
        model = User
        fields = ('username', 'password', 'first_name', 'last_name', 'groups')
        exclude = ['user_permissions', 'last_login']
        widgets = {
            'password': PasswordInput(
                attrs={
                    'placeholder': 'Ingrese su contraseña',
                }
            ),
            'username': TextInput(
                attrs={
                    'placeholder': 'Ingrese su nombre de usuario',
                }
            ),
            'first_name': TextInput(
                attrs={
                    'placeholder': 'Ingrese su nombre',
                }
            ),
            'last_name': TextInput(
                attrs={
                    'placeholder': 'Ingrese sus apellidos',
                }
            ),
        }