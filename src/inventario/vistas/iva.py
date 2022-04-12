from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from inventario.models import IVA


class IVAListView(ListView):
    model = IVA
    context_object_name = 'IVA'
    template_name = 'CRUD/listado_iva.html'
    paginate_by = 10


class IVACreateView(CreateView):
    model = IVA
    fields = ['iva']


class IVAUpdateView(UpdateView):
    model = IVA
    fields = ['iva']


class IVADeleteView(DeleteView):
    model = IVA
    success_url = '/inventario/iva/'