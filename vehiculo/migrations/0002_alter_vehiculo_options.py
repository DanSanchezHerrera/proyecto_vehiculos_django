# Generated by Django 5.1.1 on 2024-11-04 05:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vehiculo', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='vehiculo',
            options={'permissions': [('visualizar_catalogo', 'Puede visualizar Catálogo de Vehículos')]},
        ),
    ]
