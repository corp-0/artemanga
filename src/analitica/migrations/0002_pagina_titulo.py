# Generated by Django 4.0.4 on 2022-05-17 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analitica', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pagina',
            name='titulo',
            field=models.CharField(default='pichula loca', max_length=200, verbose_name='Título'),
            preserve_default=False,
        ),
    ]
