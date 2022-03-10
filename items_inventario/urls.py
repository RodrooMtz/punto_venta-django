from django.urls import path
from django.urls import path
from . import views
from .views import ProductoCreateView, ProductoUpdateView, ProductoDeleteView
from login.views import LoginFormView

urlpatterns = [
    path('', views.producto, name='producto'),
    path('home/', views.home, name='home'),
    path('nuevo/', ProductoCreateView.as_view(), name='nuevo_producto'),
    path('editar/<int:pk>/', ProductoUpdateView.as_view(), name='editar_producto'),
    path('eliminar/<int:pk>/', ProductoDeleteView.as_view(), name='eliminar_producto')
]


