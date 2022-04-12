from django.urls import path
from inventario.vistas.iva import IVAListView
from inventario.vistas.otros_autores import OtrosAutoresListView
from inventario.vistas.editorial import EditorialListView
from inventario.vistas.pais import PaisListView
from inventario.vistas.genero import GeneroListView
from inventario.vistas.autor import AutorListView
from inventario.vistas.producto import ProductoListView, ProductoUpdateView, ProductoCreateView, ProductoDeleteView

urlpatterns = [
    # listados
    path('listado-producto', ProductoListView.as_view(), name='listado-producto'),
    path('listado-autor', AutorListView.as_view(), name='listado-autor'),
    path('listado-genero', GeneroListView.as_view(), name='listado-genero'),
    path('listado-pais', PaisListView.as_view(), name='listado-pais'),
    path('listado-editorial', EditorialListView.as_view(), name='listado-editorial'),
    path('listado-otro-autor', OtrosAutoresListView.as_view(), name='listado-otro-autor'),
    path('listado-iva', IVAListView.as_view(), name='listado-iva'),
    # crear
    path('crear-producto', ProductoCreateView.as_view(), name='crear-producto'),
    # editar
    path('editar-producto/<pk>/', ProductoUpdateView.as_view(), name='editar-producto'),
    # eliminar
    path('eliminar-producto/<pk>/', ProductoDeleteView.as_view(), name='eliminar-producto'),
]
