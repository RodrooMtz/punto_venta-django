from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator

from .mixins import IsSuperuserMixin
from .models import Producto
from django.views.generic import CreateView, UpdateView, DeleteView
from items_inventario.forms import CategoriaForm, ProductForm


# Create your views here.

@login_required(login_url='login')
def producto(request):
    productos_ = Producto.objects.all()
    context = {
        'productos_': productos_,
    }
    return render(request, 'producto/list.html', context)


@login_required(login_url='login')
def home(request):
    return render(request, 'include/bienvenido.html')


class ProductoCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    permission_required = 'items_inventario.view_producto'
    model = Producto
    form_class = ProductForm
    template_name = 'producto/create.html'
    success_url = reverse_lazy('producto')

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


class ProductoUpdateView(UpdateView):
    model = Producto
    form_class = ProductForm
    template_name = 'producto/create.html'
    success_url = reverse_lazy('producto')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


class ProductoDeleteView(DeleteView):
    model = Producto
    template_name = 'producto/delete.html'
    success_url = reverse_lazy('producto')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


