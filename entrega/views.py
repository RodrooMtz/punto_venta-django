from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator

from .models import Entrega
from django.views.generic import CreateView, UpdateView, DeleteView
from items_inventario.forms import EntregaForm


@login_required(login_url='login')
def entrega(request):
    productos_ = Entrega.objects.all()
    context = {
        'productos_': productos_,
    }
    return render(request, 'entrega/list2.html', context)


class EntregaCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    permission_required = 'items_inventario.view_producto'
    model = Entrega
    form_class = EntregaForm
    template_name = 'entrega/crear.html'
    success_url = reverse_lazy('entrega')

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


class EntregaUpdateView(UpdateView):
    model = Entrega
    form_class = EntregaForm
    template_name = 'entrega/crear.html'
    success_url = reverse_lazy('entrega')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


class EntregaDeleteView(DeleteView):
    model = Entrega
    template_name = 'entrega/eliminar.html'
    success_url = reverse_lazy('entrega')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
