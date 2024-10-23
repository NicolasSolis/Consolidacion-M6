from django.db import models

class VehiculoModel(models.Model):
    MARCA_CHOICES = [
        ('Fiat', 'Fiat'),
        ('Chevrolet', 'Chevrolet'),
        ('Ford', 'Ford'),
        ('Toyota', 'Toyota'),
    ]

    CATEGORIA_CHOICES = [
        ('Particular', 'Particular'),
        ('Transporte', 'Transporte'),
        ('Carga', 'Carga'),
    ]

    marca = models.CharField(max_length=20, choices=MARCA_CHOICES, default='Ford')
    modelo = models.CharField(max_length=100)
    serial_carroceria = models.CharField(max_length=50)
    serial_motor = models.CharField(max_length=50)
    categoria = models.CharField(max_length=20, choices=CATEGORIA_CHOICES, default='Particular')
    precio = models.IntegerField()
    fecha_de_creacion = models.DateTimeField(auto_now=False, auto_now_add=True)
    fecha_de_modificacion = models.DateTimeField(auto_now=True, auto_now_add=False)

    @property
    def condicion_precio(self):
        if self.precio < 10000:
            return "Bajo"
        elif 10000 <= self.precio <= 30000:
            return "Medio"
        else:
            return "Alto"

    class Meta: #no sabía si era mala traducción de la pauta, pero añadí un view_vehiculomodel redundante
        verbose_name = "vehículo"
        verbose_name_plural= 'vehículos'
        ordering = ['-fecha_de_modificacion']
        permissions = [
            ("can_visualizar_catalogo", "Puede ver catálogo")
        ]

    def __str__(self):
        return self.modelo