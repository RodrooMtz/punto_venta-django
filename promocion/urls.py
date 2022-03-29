from django.urls import path
from django.urls import path
from . import views
from .views import PromocionCreateView, PromocionUpdateView, PromocionDeleteView, ProductosDiasCreateView
from login.views import LoginFormView

urlpatterns = [
    path('nuevo/', PromocionCreateView.as_view(), name='nuevo_promocion'),
    path('editar/<int:pk>/', PromocionUpdateView.as_view(), name='editar_promocion'),
    path('eliminar/<int:pk>/', PromocionDeleteView.as_view(), name='eliminar_promocion'),
    path('agregar_producto_promocion', ProductosDiasCreateView.as_view(), name='agregar_producto_promocion')

]