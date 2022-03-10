from django.urls import path
from django.urls import path
from . import views
from login.views import LoginFormView

urlpatterns = [
    path('', views.carta, name='carta'),

]