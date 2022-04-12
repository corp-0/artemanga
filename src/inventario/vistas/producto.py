from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, CreateView, DeleteView

from inventario.models import Producto


class ProductoListView(ListView):
    model = Producto
    template_name = 'CRUD/listado_producto.html'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        contexto_extra = {
            'url_crear': 'crear-producto',
            'boton_crear': 'Crear producto',
            'url_editar': 'editar-producto',
            'url_eliminar': 'eliminar-producto',
        }

        context.update(contexto_extra)
        return context


class ProductoUpdateView(UpdateView):
    model = Producto
    template_name = 'CRUD/form_generico.html'
    fields = '__all__'
    success_url = reverse_lazy('listado-productos')


class ProductoCreateView(CreateView):
    model = Producto
    template_name = 'CRUD/form_generico.html'
    fields = '__all__'
    success_url = reverse_lazy('listado-productos')


class ProductoDeleteView(DeleteView):
    model = Producto
    template_name = 'CRUD/eliminar_generico.html'
    success_url = reverse_lazy('listado-productos')