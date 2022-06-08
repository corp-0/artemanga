from django.urls import path
from .views import TicketDetalle, CerrarTicket, ReabrirTicket, TicketsAbiertosLisView, TicketsCerradosLisView, MisTicketsView

urlpatterns = [
    path('listado-ticket-abierto', TicketsAbiertosLisView.as_view(), name='listado-ticket-abierto'),
    path('listado-ticket-cerrado', TicketsCerradosLisView.as_view(), name='listado-ticket-cerrado'),

    path('mis-tickets', MisTicketsView.as_view(), name='mis-tickets'),
    path('detalle/<pk>', TicketDetalle.as_view(), name='contacto-detalle'),
    path('cerrar/<pk>', CerrarTicket.as_view(), name='contacto-cerrar'),
    path('reabrir/<pk>', ReabrirTicket.as_view(), name='contacto-reabrir'),
]