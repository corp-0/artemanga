from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from inventario.models import Autor


class AutorListView(ListView):
    model = Autor
    context_object_name = 'Autores'
    template_name = 'CRUD/listado_autor.html'
    paginate_by = 10


class AutorCreateView(CreateView):
    model = Autor
    fields = ['nombre', 'apellido', 'es_activo']


class AutorUpdateView(UpdateView):
    model = Autor
    fields = ['nombre', 'apellido', 'es_activo']


class AutorDeleteView(DeleteView):
    model = Autor
    success_url = '/inventario/autor/'