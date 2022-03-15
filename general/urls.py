from django.urls import path
from .views import GeneralCreateView, GeneralUpdateView, GeneralDeleteView

urlpatterns = [
    path('nuevo/', GeneralCreateView.as_view(), name='nuevo_general'),
    path('editar/<int:pk>/', GeneralUpdateView.as_view(), name='editar_general'),
    path('eliminar/<int:pk>/', GeneralDeleteView.as_view(), name='eliminar_general')
]