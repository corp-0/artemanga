# Generated by Django 4.0.3 on 2022-04-17 22:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('despacho', '0018_alter_direccion_codigo_postal'),
    ]

    operations = [
        migrations.AlterField(
            model_name='direccion',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='direcciones', to=settings.AUTH_USER_MODEL),
        ),
    ]
