from django.urls import path
from inventario.views import (
    AutorListView, GeneroListView, PaisListView, EditorialListView,
    OtrosAutoresListView, IVAListView, ProductoListView, ProductoCreateView,
    ProductoUpdateView, ProductoDeleteView
)

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
