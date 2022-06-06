from django.db import models
from cuenta_usuario.models import Usuario
from venta.models import Venta
from .enums.estado_ticket import ESTADO_TICKET_CHOICES, EstadoTicket
from .enums.tipo_ticket import TIPO_TICKET_CHOICES, TipoTicket


class Ticket(models.Model):
    id = models.AutoField(primary_key=True)
    tipo = models.PositiveSmallIntegerField(choices=TIPO_TICKET_CHOICES, default=TipoTicket.AYUDA.value)
    fecha_creacion = models.DateTimeField(verbose_name="fecha de creacion", auto_now_add=True)
    fecha_modificacion = models.DateTimeField(verbose_name="fecha de modificacion", auto_now=True)
    estado = models.PositiveSmallIntegerField(choices=ESTADO_TICKET_CHOICES, default=EstadoTicket.ABIERTO.value)
    # conexiones
    venta = models.ForeignKey(Venta, on_delete=models.CASCADE, blank=True, null=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    @property
    def tipo_ticket_humanizado(self):
        return TipoTicket(self.tipo).name.title()

    @property
    def estado_ticket_humanizado(self):
        return EstadoTicket(self.estado).name.title()


class Mensaje(models.Model):
    id = models.AutoField(primary_key=True)
    fecha_creacion = models.DateTimeField(verbose_name="fecha de creacion", auto_now_add=True)
    texto = models.CharField(max_length=200, verbose_name="texto")
    # conexiones
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)


class Respuesta(models.Model):
    id = models.AutoField(primary_key=True)
    fecha_creacion = models.DateTimeField(verbose_name="fecha de creacion", auto_now_add=True)
    texto = models.CharField(max_length=200, verbose_name="texto")
    # conexiones
    mensaje = models.OneToOneField(Mensaje, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
