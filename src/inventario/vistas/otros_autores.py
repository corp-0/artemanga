from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from inventario.models import OtrosAutores


class OtrosAutoresListView(ListView):
    model = OtrosAutores
    context_object_name = 'Otros Autores'
    template_name = 'CRUD/listado_otro_autor.html'
    paginate_by = 10


class OtrosAutoresCreateView(CreateView):
    model = OtrosAutores
    fields = ['nombre', 'cargo']


class OtrosAutoresUpdateView(UpdateView):
    model = OtrosAutores
    fields = ['nombre', 'cargo']


class OtrosAutoresDeleteView(DeleteView):
    model = OtrosAutores
    success_url = '/inventario/otro_autor/'