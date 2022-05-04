from django import template
from inventario.models import Producto
from catalogo.carrito.models import Carrito

register = template.Library()

@register.simple_tag
def carrito_nombre_producto(id: int):
    producto: Producto = Producto.objects.get(pk=id)
    return producto.titulo_es

@register.simple_tag(takes_context=True)
def carrito_precio_unitario_producto(context, id: int):
    producto: Producto = Producto.objects.get(pk=id)
    return producto.precio

@register.simple_tag(takes_context=True)
def carrito_precio_total_producto(context, id: int):
    carrito: Carrito = Carrito.deserializar(context['carrito'])
    return carrito.total_producto(id)

@register.simple_tag(takes_context=True)
def carrito_total(context):
    carrito: Carrito = Carrito.deserializar(context['carrito'])
    if not carrito.productos:
        return 0
    return carrito.total