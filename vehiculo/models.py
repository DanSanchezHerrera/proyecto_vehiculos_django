from django.db import models
from django.utils import timezone

class Vehiculo(models.Model):
    MARCAS = [
        ('Fiat', 'Fiat'),
        ('Chevrolet', 'Chevrolet'),
        ('Ford', 'Ford'),
        ('Toyota', 'Toyota'),
    ]

    CATEGORIAS = [
        ('Particular', 'Particular'),
        ('Transporte', 'Transporte'),
        ('Carga', 'Carga'),
    ]

    marca = models.CharField(
        max_length=20,
        choices=MARCAS,
        default='Ford'
    )
    modelo = models.CharField(max_length=100)
    serial_carroceria = models.CharField(max_length=50)
    serial_motor = models.CharField(max_length=50)
    categoria = models.CharField(
        max_length=20,
        choices=CATEGORIAS,
        default='Particular'
    )
    precio = models.IntegerField()
    fecha_de_creacion = models.DateTimeField(default=timezone.now)
    fecha_de_modificacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.marca} {self.modelo}"