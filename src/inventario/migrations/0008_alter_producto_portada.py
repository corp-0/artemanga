# Generated by Django 4.0.4 on 2022-05-04 02:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0007_producto_es_nuevo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='portada',
            field=models.ImageField(blank=True, default='portadas/portada.jpg', upload_to='portadas', verbose_name='portada'),
        ),
    ]
