# Generated by Django 4.0.4 on 2022-05-26 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('venta', '0002_alter_venta_usuario'),
    ]

    operations = [
        migrations.AddField(
            model_name='venta',
            name='boleta',
            field=models.FileField(blank=True, null=True, upload_to='boletas/'),
        ),
    ]
