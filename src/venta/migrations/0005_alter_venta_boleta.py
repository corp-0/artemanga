# Generated by Django 4.0.4 on 2022-05-28 01:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('venta', '0004_despacho_codigo_seguimiento_alter_venta_boleta'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venta',
            name='boleta',
            field=models.FileField(blank=True, null=True, upload_to='boletas/'),
        ),
    ]
