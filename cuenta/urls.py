from django.urls import path
from . import views
from .views import SaleCreateView, cuenta
from login.views import LoginFormView

urlpatterns = [
    path('crear/', SaleCreateView.as_view(), name='crear_cuenta'),
    path('cuenta/', views.cuenta, name='cuenta'),
    path('mesero/', views.mesero, name='mesero'),
    path('estadisticas/', views.estadisticas, name='estadisticas'),
]