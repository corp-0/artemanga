from django.contrib.auth.models import AbstractUser
from django.db import models
from .tipo_enum.tipo_usuario import TIPO_CHOICES, Tipo


class Usuario(AbstractUser):
    id = models.AutoField(primary_key=True)
    primer_nombre = models.CharField(max_length=200, verbose_name="primer nombre", db_index=True)
    segundo_nombre = models.CharField(max_length=200, verbose_name="segundo nombre", blank=True)
    primer_apellido = models.CharField(max_length=200, verbose_name="primer apellido", db_index=True)
    segundo_apellido = models.CharField(max_length=200, verbose_name="segundo apellido", blank=True)
    fecha_registro = models.DateField()
    es_activo = models.BooleanField(default=True)
    ultimo_ingreso = models.DateField()
    tipo_usuario = models.PositiveSmallIntegerField(choices=TIPO_CHOICES, default=Tipo.CLIENTE.value)

    def __str__(self):
        return f"{self.id}"

    def es_ventas(self) -> bool:
        return self.tipo_usuario == Tipo.VENTAS.value

    def es_bodega(self) -> bool:
        return self.tipo_usuario == Tipo.BODEGA.value

    def es_sysadmin(self) -> bool:
        return self.tipo_usuario == Tipo.ADMINISTRADOR.value

    def es_cliente(self) -> bool:
        return self.tipo_usuario <= Tipo.CLIENTE.value

    def generar_pass_temporal_empleados(self) -> str:
        ident = f"{str(self.id).zfill(2)[:2]}"
        primer_nombre = f"{self.primer_nombre.upper()[:2]}"
        primer_apellido = f"{self.primer_apellido.lower()[-2:]}"
        fecha_registro = f"{self.fecha_registro[-2:]}"
        return f"{ident}{primer_nombre}{primer_apellido}{fecha_registro}"
