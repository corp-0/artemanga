from django.core.management import call_command
from django.core.management.base import BaseCommand

from cuenta_usuario.models import Usuario


class Command(BaseCommand):
    help = 'Genera toda la shiet de datos prueba'

    def handle(self, *args, **options):
        self.preparar_base_de_datos()
        self.generar_admin()
        self.generar_clientes()
        self.generar_inventario()
        self.generar_ventas()

    def preparar_base_de_datos(self):
        print('Limpiando datos en base de datos...')
        call_command('flush', interactive=False)
        print('Inicializando datos en base de datos...')
        call_command('migrate', interactive=False)

    def generar_admin(self):
        print('Generando admin...')
        admin = Usuario.objects.create_superuser(
            username='admin',
            email='admin@admin.com',
            password='admin',
            primer_nombre='admin',
            primer_apellido='admin',
            tipo_usuario=1
        )

        admin.save()

    def generar_clientes(self):
        call_command('generar_clientes')

    def generar_inventario(self):
        call_command('generar_inventario')

    def generar_ventas(self):
        call_command('generar_ventas')
