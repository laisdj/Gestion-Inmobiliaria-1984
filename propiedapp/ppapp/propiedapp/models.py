from django.db import models
from django.contrib.auth.models import User

class Region(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    
    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name_plural = "Regiones"

class Comuna(models.Model):
    nombre = models.CharField(max_length=100)
    region = models.ForeignKey(Region, on_delete=models.CASCADE, related_name='comunas')
    
    def __str__(self):
        return f"{self.nombre} - {self.region.nombre}"
    
    class Meta:
        unique_together = ('nombre', 'region')
        verbose_name_plural = "Comunas"

class Propiedad(models.Model):
    TIPO_CHOICES = [
        ('casa', 'Casa'),
        ('departamento', 'Departamento'),
        ('sitio', 'Sitio'),
        ('bodega', 'Bodega'),
        ('espacio_seguro', 'Espacio Seguro'),
        ('estacionamiento', 'Estacionamiento'),
        ('oficina', 'Oficina'),
    ]

    titulo = models.CharField(max_length=200)
    descripcion = models.TextField(blank=True, null=True)
    precio = models.DecimalField(max_digits=10, decimal_places=0)
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES)
    
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    
    region = models.ForeignKey(Region, on_delete=models.PROTECT)
    comuna = models.ForeignKey(Comuna, on_delete=models.PROTECT)
    
    metros_construidos = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    metros_terreno = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    
    habitaciones = models.IntegerField(default=0)
    banos = models.IntegerField(default=0)
    
    fecha_publicacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo