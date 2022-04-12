from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from inventario.models import Editorial


class EditorialListView(ListView):
    model = Editorial
    context_object_name = 'Editoriales'
    template_name = 'CRUD/listado_editorial.html'
    paginate_by = 10


class EditorialCreateView(CreateView):
    model = Editorial
    fields = ['nombre']


class EditorialUpdateView(UpdateView):
    model = Editorial
    fields = ['nombre']


class EditorialDeleteView(DeleteView):
    model = Editorial
    success_url = '/inventario/editorial/'