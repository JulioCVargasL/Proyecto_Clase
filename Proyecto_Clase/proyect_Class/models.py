from django.db import models

# Create your models here.

class Aprendiz(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    edad = models.IntegerField()
    telefono = models.CharField(max_length=20)
    correo = models.EmailField()
    ficha = models.IntegerField()

class Etapa(models.Model):
    induccion = models.CharField(max_length=20)
    electiva = models.TextField()
    productiva = models.TextField()

