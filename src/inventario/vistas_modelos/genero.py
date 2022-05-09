from django.urls import reverse_lazy

from artemangaweb.mixins import MensajeResultadoFormMixin, VistaRestringidaMixin
from cuenta_usuario.enums.opciones import TipoUsuario
from inventario.models import Genero
from .vistas_genericas import CrearGenericoView, ActualizarGenericoView, EliminarGenericoView, ListaGenericaView

EXITO_URL = reverse_lazy('listado-genero')


class GeneroListView(VistaRestringidaMixin, ListaGenericaView):
    usuarios_permitidos = [TipoUsuario.ADMINISTRADOR, TipoUsuario.BODEGA]
    model = Genero
    template_name = 'administración/CRUD/listado_genero.html'
    paginate_by = 10
    ordering = ['id']
    context_object_name = 'generos'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        contexto_extra = {
            'url_crear': 'crear-genero',
            'url_editar': 'editar-genero',
            'url_eliminar': 'eliminar-genero',
        }

        context.update(contexto_extra)
        return context


class GeneroCreateView(VistaRestringidaMixin, CrearGenericoView):
    usuarios_permitidos = [TipoUsuario.ADMINISTRADOR, TipoUsuario.BODEGA]
    model = Genero
    success_url = EXITO_URL


class GeneroUpdateView(VistaRestringidaMixin, ActualizarGenericoView):
    usuarios_permitidos = [TipoUsuario.ADMINISTRADOR, TipoUsuario.BODEGA]
    model = Genero
    success_url = EXITO_URL


class GeneroDeleteView(VistaRestringidaMixin, EliminarGenericoView):
    usuarios_permitidos = [TipoUsuario.ADMINISTRADOR, TipoUsuario.BODEGA]
    model = Genero
    success_url = EXITO_URL
