# Generated by Django 4.0.3 on 2022-04-09 01:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reportes',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('fecha_creacion', models.DateTimeField(verbose_name='fecha de creacion')),
                ('reporte', models.JSONField(verbose_name='reporte')),
            ],
        ),
    ]