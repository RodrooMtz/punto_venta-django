from django.urls import path
from django.urls import path
from . import views
from .views import ProveedorCreateView, ProveedorUpdateView, ProveedorDeleteView
from login.views import LoginFormView

urlpatterns = [
    path('', views.proveedor, name='proveedor'),
    path('nuevo/', ProveedorCreateView.as_view(), name='nuevo_proveedor'),
    path('editar/<int:pk>/', ProveedorUpdateView.as_view(), name='editar_proveedor'),
    path('eliminar/<int:pk>/', ProveedorDeleteView.as_view(), name='eliminar_proveedor')
]