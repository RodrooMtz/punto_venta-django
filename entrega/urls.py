from django.urls import path
from . import views
from .views import EntregaCreateView, EntregaUpdateView, EntregaDeleteView
from login.views import LoginFormView

urlpatterns = [
    path('', views.entrega, name='entrega'),
    path('nuevo/', EntregaCreateView.as_view(), name='nuevo_entrega'),
    path('editar/<int:pk>/', EntregaUpdateView.as_view(), name='editar_entrega'),
    path('eliminar/<int:pk>/', EntregaDeleteView.as_view(), name='eliminar_entrega')
]