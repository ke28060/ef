from django.db import models

# Create your models here.

class Pais(models.Model):
    codigo = models.TextField()
    nombre = models.TextField()
    poblacion = models.TextField()
    estado = models.BooleanField()
class editorial(models.Model):
    nombre = models.TextField()
    url = models.TextField()
    imagen = models.ImageField(default='null', verbose_name="miniature")
    estado = models.BooleanField()