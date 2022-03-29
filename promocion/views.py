from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from carta.models import ProductoMenu
from promocion.models import Promocion, ProductosDias
from django.views.generic import CreateView, UpdateView, DeleteView
from inventario.forms import PromocionForm, ProductosDiasForm


class PromocionCreateView(CreateView):
    model = Promocion
    second_model = ProductosDias
    form_class = PromocionForm
    second_form_class = PromocionForm
    template_name = 'promocion/crear.html'
    success_url = reverse_lazy('inventario')

    @method_decorator(login_required)
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'add':
                print(request.FILES)
                form = self.get_form()
                if form.is_valid():
                    form.save()
                else:
                    data['error'] = form.errors
            else:
                data['error'] = 'No ha seleccionado una opción'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Nueva Promoción'
        context['action'] = 'add'
        context['list_url'] = self.success_url
        return context


class PromocionUpdateView(UpdateView):
    model = Promocion
    form_class = PromocionForm
    template_name = 'promocion/crear.html'
    success_url = reverse_lazy('inventario')

    @method_decorator(login_required)
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'edit':
                form = self.get_form()
                if form.is_valid():
                    form.save()
                else:
                    data['error'] = form.errors
            else:
                data['error'] = 'No ha '
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action'] = 'edit'
        context['list_url'] = self.success_url
        context['title'] = 'Editar Promoción'
        return context


class PromocionDeleteView(DeleteView):
    model = Promocion
    template_name = 'promocion/eliminar.html'
    success_url = reverse_lazy('inventario')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminar Promoción'
        return context


class ProductosDiasCreateView(CreateView):
    model = ProductosDias
    form_class = ProductosDiasForm
    template_name = 'promocion/editar.html'
    success_url = reverse_lazy('inventario')

    @method_decorator(login_required)
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'edit':
                print(request.FILES)
                form = self.get_form()
                if form.is_valid():
                    form.save()
                else:
                    data['error'] = form.errors
            else:
                data['error'] = 'No ha seleccionado una opción'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Nuevo Producto'
        context['action'] = 'edit'
        context['list_url'] = self.success_url
        return context