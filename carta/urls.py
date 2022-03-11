from django.urls import path
from . import views
from login.views import LoginFormView
from .views import PlatilloCreateView, PlatilloUpdateView, PlatilloDeleteView

urlpatterns = [
    path('nuevo/', PlatilloCreateView.as_view(), name='nuevo_platillo'),
    path('editar/<int:pk>/', PlatilloUpdateView.as_view(), name='editar_platillo'),
    path('eliminar/<int:pk>/', PlatilloDeleteView.as_view(), name='eliminar_platillo')
]