# Generated by Django 5.1.1 on 2024-11-04 05:01

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vehiculo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marca', models.CharField(choices=[('Fiat', 'Fiat'), ('Chevrolet', 'Chevrolet'), ('Ford', 'Ford'), ('Toyota', 'Toyota')], default='Ford', max_length=20)),
                ('modelo', models.CharField(max_length=100)),
                ('serial_carroceria', models.CharField(max_length=50)),
                ('serial_motor', models.CharField(max_length=50)),
                ('categoria', models.CharField(choices=[('Particular', 'Particular'), ('Transporte', 'Transporte'), ('Carga', 'Carga')], default='Particular', max_length=20)),
                ('precio', models.IntegerField()),
                ('fecha_de_creacion', models.DateTimeField(default=django.utils.timezone.now)),
                ('fecha_de_modificacion', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
