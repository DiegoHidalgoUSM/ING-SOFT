from django.db import models
from django.contrib.auth.models import User

class Categoria(models.Model):
    nombre = models.CharField(max_length=20)
    descripcion = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Comunicado(models.Model):
    NIVEL_CHOICES = [
        ("GEN", "General"),
        ("PRE", "Ciclo Preescolar"),
        ("BAS", "Ciclo Básico"),
        ("MED", "Ciclo Medio"),
    ]
    titulo = models.CharField(max_length=20)
    detalle = models.CharField(max_length=50)
    fecha_envio = models.DateField()
    nivel = models.CharField(max_length=3, choices=NIVEL_CHOICES)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    fecha_ultima_modificacion = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, default=None)

    def __str__(self):
        return self.titulo


