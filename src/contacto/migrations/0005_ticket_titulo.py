# Generated by Django 4.0.5 on 2022-06-07 21:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacto', '0004_alter_mensaje_texto'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='titulo',
            field=models.CharField(default='Pichula', max_length=100, verbose_name='Breve descripción de este ticket'),
            preserve_default=False,
        ),
    ]