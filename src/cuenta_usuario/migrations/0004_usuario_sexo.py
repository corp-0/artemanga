# Generated by Django 4.0.3 on 2022-04-16 22:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cuenta_usuario', '0003_alter_usuario_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='sexo',
            field=models.PositiveSmallIntegerField(choices=[[1, 'Masculino'], [2, 'Femenino'], [3, 'Otro'], [4, 'No_responde']], default=1),
        ),
    ]
