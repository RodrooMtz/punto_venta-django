from django.urls import path
from django.urls import path
from . import views
from .views import UserCreateView, UserUpdateView, UserDeleteView
from login.views import LoginFormView

urlpatterns = [
    path('', views.user, name='user'),
    path('nuevo/', UserCreateView.as_view(), name='nuevo_user'),
    path('editar/<int:pk>/', UserUpdateView.as_view(), name='editar_user'),
    path('eliminar/<int:pk>/', UserDeleteView.as_view(), name='eliminar_user')
]