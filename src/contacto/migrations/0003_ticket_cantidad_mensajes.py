# Generated by Django 4.0.5 on 2022-06-07 21:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacto', '0002_delete_respuesta'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='cantidad_mensajes',
            field=models.PositiveSmallIntegerField(default=0),
        ),
    ]
