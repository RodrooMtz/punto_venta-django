from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator

from carta.models import ProductoMenu
from .models import Inventario
from django.views.generic import CreateView, UpdateView, DeleteView
from inventario.forms import CategoriaForm


# Create your views here.

@login_required(login_url='login')
def inventario(request):
    categorias = Inventario.objects.all()
    # proveedores = Proveedor.objects.all()
    platillos = ProductoMenu.objects.all()
    context = {
        'categorias': categorias,
        # 'proveedor': proveedores,
        'platillos': platillos,
    }
    return render(request, 'include/list2.html', context)


class CategoriaCreateView(CreateView):
    model = Inventario
    form_class = CategoriaForm
    template_name = 'formulario/categoria.html'
    success_url = reverse_lazy('inventario')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


class CategoryUpdateView(UpdateView):
    model = Inventario
    form_class = CategoriaForm
    template_name = 'formulario/categoria.html'
    success_url = reverse_lazy('inventario')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


class CategoriaDeleteView(DeleteView):
    model = Inventario
    template_name = 'formulario/eliminar.html'
    success_url = reverse_lazy('inventario')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
