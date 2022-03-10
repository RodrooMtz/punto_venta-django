from django.urls import path
from django.urls import path
from . import views
from .views import CategoriaCreateView, CategoryUpdateView, CategoriaDeleteView
from login.views import LoginFormView

urlpatterns = [
    path('', views.inventario, name='inventario'),
    path('home/', views.home, name='home'),
    path('nuevo/', CategoriaCreateView.as_view(), name='nuevo'),
    path('editar/<int:pk>/', CategoryUpdateView.as_view(), name='editar'),
    path('eliminar/<int:pk>/', CategoriaDeleteView.as_view(), name='eliminar')
]