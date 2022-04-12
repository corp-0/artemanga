from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from inventario.models import Pais


class PaisListView(ListView):
    model = Pais
    context_object_name = 'Paises'
    template_name = 'CRUD/listado_pais.html'
    paginate_by = 10


class PaisCreateView(CreateView):
    model = Pais
    fields = ['nombre']


class PaisUpdateView(UpdateView):
    model = Pais
    fields = ['nombre']


class PaisDeleteView(DeleteView):
    model = Pais
    success_url = '/inventario/pais/'