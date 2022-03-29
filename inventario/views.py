from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from carta.models import ProductoMenu
from general.models import General
from promocion.models import Promocion, ProductosDias
from .mixins import ValidatePermissionRequiredMixin
from .models import Inventario
from django.views.generic import CreateView, UpdateView, DeleteView
from inventario.forms import CategoriaForm


@login_required(login_url='login')
def inventario(request):
    categorias = Inventario.objects.all()
    promociones = Promocion.objects.all()
    producto_promocion = ProductosDias.objects.all()
    platillos = ProductoMenu.objects.all()
    general = General.objects.all()

    context = {
        'categorias': categorias,
        'promociones': promociones,
        'platillos': platillos,
        'generales': general,
        'producto_promocion': producto_promocion,
    }
    return render(request, 'include/list2.html', context)


class CategoriaCreateView(ValidatePermissionRequiredMixin, CreateView):
    permission_required = 'inventario.add_inventario'
    model = Inventario
    form_class = CategoriaForm
    template_name = 'formulario/categoria.html'
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
        # data['name'] = categoria.nombre_categoria

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Nueva Categoría'
        context['action'] = 'add'
        context['list_url'] = self.success_url
        return context


class CategoryUpdateView(ValidatePermissionRequiredMixin, UpdateView):
    permission_required = 'inventario.change_inventario'
    model = Inventario
    form_class = CategoriaForm
    template_name = 'formulario/categoria.html'
    success_url = reverse_lazy('inventario')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
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
        context['title'] = 'Editar Categoría'
        context['action'] = 'edit'
        context['list_url'] = self.success_url
        return context


class CategoriaDeleteView(ValidatePermissionRequiredMixin, DeleteView):
    permission_required = 'inventario.delete_inventario'
    model = Inventario
    template_name = 'formulario/eliminar.html'
    success_url = reverse_lazy('inventario')

    @method_decorator(login_required)
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            self.object.delete()
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminar Categoría'
        context['action'] = 'delete'
        context['list_url'] = self.success_url
        return context
