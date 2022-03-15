from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator

from carta.models import ProductoMenu
from promocion.models import Promocion, ProductosDias
from django.views.generic import CreateView, UpdateView, DeleteView
from inventario.forms import PromocionForm, Promocion1Form


class PromocionCreateView(CreateView):
    model = Promocion
    form_class = Promocion1Form
    second_form_class = PromocionForm
    template_name = 'promocion/crear.html'
    success_url = reverse_lazy('inventario')

    def get_context_data(self, **kwargs):
        context = super(PromocionCreateView, self).get_context_data(**kwargs)
        if 'form' not in context:
            context['form'] = self.form_class(self.request.GET)
        if 'form2' not in context:
            context['form2'] = self.second_form_class(self.request.GET)
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        form = self.form_class(request.POST)
        form2 = self.second_form_class(request.POST)
        if form.is_valid() and form2.is_valid():
            solicitud = form.save(commit=False)
            solicitud.persona = form2.save()
            solicitud.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form=form, form2=form2))


    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


class PromocionUpdateView(UpdateView):
    model = ProductosDias
    form_class = PromocionForm
    template_name = 'promocion/crear.html'
    success_url = reverse_lazy('inventario')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


class PromocionDeleteView(DeleteView):
    model = ProductosDias
    template_name = 'promocion/eliminar.html'
    success_url = reverse_lazy('inventario')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
