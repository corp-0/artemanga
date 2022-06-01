# Generated by Django 4.0.4 on 2022-06-01 02:03

import contacto.tipo_enum.tipo_ticket
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('venta', '0005_alter_venta_boleta'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Mensaje',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('fecha_creacion', models.DateTimeField(verbose_name='fecha de creacion')),
                ('texto', models.CharField(max_length=200, verbose_name='texto')),
            ],
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('tipo', models.PositiveSmallIntegerField(choices=[[1, 'Duda'], [2, 'Sugerencia'], [3, 'Queja']], default=contacto.tipo_enum.tipo_ticket.TipoTicket['SUGERENCIA'])),
                ('fecha_creacion', models.DateTimeField(verbose_name='fecha de creacion')),
                ('fecha_modificacion', models.DateTimeField(verbose_name='fecha de modificacion')),
                ('estado', models.PositiveSmallIntegerField(choices=[[1, 'Pendiente'], [2, 'Resuelto'], [3, 'Cancelado']], default=1)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('venta', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='venta.venta')),
            ],
        ),
        migrations.CreateModel(
            name='Respuesta',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('fecha_creacion', models.DateTimeField(verbose_name='fecha de creacion')),
                ('texto', models.CharField(max_length=200, verbose_name='texto')),
                ('mensaje', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='contacto.mensaje')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='mensaje',
            name='ticket',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contacto.ticket'),
        ),
        migrations.AddField(
            model_name='mensaje',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
