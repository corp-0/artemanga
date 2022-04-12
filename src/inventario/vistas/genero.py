from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from inventario.models import Genero


class GeneroListView(ListView):
    model = Genero
    context_object_name = 'Generos'
    template_name = 'CRUD/listado_genero.html'
    paginate_by = 10


class GeneroCreateView(CreateView):
    model = Genero
    fields = ['nombre']


class GeneroUpdateView(UpdateView):
    model = Genero
    fields = ['nombre']


class GeneroDeleteView(DeleteView):
    model = Genero
    success_url = '/inventario/genero/'