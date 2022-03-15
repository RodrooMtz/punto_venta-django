from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator

from carta.models import ProductoMenu
from general.models import General
from promocion.models import Promocion, ProductosDias
from .models import General
from django.views.generic import CreateView, UpdateView, DeleteView
from inventario.forms import CategoriaForm, GeneralForm


class GeneralCreateView(CreateView):
    model = General
    form_class = GeneralForm
    template_name = 'general/crear.html'
    success_url = reverse_lazy('inventario')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Nuevo Registro'
        return context


class GeneralUpdateView(UpdateView):
    model = General
    form_class = GeneralForm
    template_name = 'general/crear.html'
    success_url = reverse_lazy('inventario')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Editar Registro'
        return context


class GeneralDeleteView(DeleteView):
    model = General
    template_name = 'general/eliminar.html'
    success_url = reverse_lazy('inventario')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminar Registro'
        return context