# Generated by Django 4.0.5 on 2022-06-18 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0011_alter_producto_numero_paginas_alter_producto_precio_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='numero_paginas',
            field=models.PositiveIntegerField(verbose_name='número de paginas'),
        ),
    ]