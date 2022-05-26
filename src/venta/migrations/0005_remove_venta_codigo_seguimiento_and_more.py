# Generated by Django 4.0.4 on 2022-05-26 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('venta', '0004_venta_codigo_seguimiento'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='venta',
            name='codigo_seguimiento',
        ),
        migrations.AddField(
            model_name='despacho',
            name='codigo_seguimiento',
            field=models.CharField(blank=True, max_length=100, verbose_name='codigo de seguimiento Starken'),
        ),
    ]
