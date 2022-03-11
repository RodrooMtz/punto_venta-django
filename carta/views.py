from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import UpdateView, DeleteView, CreateView

from carta.models import ProductoMenu
from inventario.forms import CartaForm
from inventario.models import Inventario


class PlatilloCreateView(CreateView):
    model = ProductoMenu
    form_class = CartaForm
    template_name = 'carta/crear.html'
    success_url = reverse_lazy('inventario')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


class PlatilloUpdateView(UpdateView):
    model = ProductoMenu
    form_class = CartaForm
    template_name = 'carta/crear.html'
    success_url = reverse_lazy('inventario')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


class PlatilloDeleteView(DeleteView):
    model = ProductoMenu
    template_name = 'carta/eliminar.html'
    success_url = reverse_lazy('inventario')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context