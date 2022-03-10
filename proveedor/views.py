from django.shortcuts import render

# Create your views here.
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator

from .models import Proveedor
from django.views.generic import CreateView, UpdateView, DeleteView
from items_inventario.forms import ProveedorForm


# Create your views here.

@login_required(login_url='login')
def proveedor(request):
    productos_ = Proveedor.objects.all()
    context = {
        'productos_': productos_,
    }
    return render(request, 'proveedor/list2.html', context)


@login_required(login_url='login')
def home(request):
    return render(request, 'include/bienvenido.html')


class ProveedorCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    permission_required = 'items_inventario.view_producto'
    model = Proveedor
    form_class = ProveedorForm
    template_name = 'proveedor/crear.html'
    success_url = reverse_lazy('proveedor')

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


class ProveedorUpdateView(UpdateView):
    model = Proveedor
    form_class = ProveedorForm
    template_name = 'proveedor/crear.html'
    success_url = reverse_lazy('proveedor')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


class ProveedorDeleteView(DeleteView):
    model = Proveedor
    template_name = 'proveedor/eliminar.html'
    success_url = reverse_lazy('proveedor')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context