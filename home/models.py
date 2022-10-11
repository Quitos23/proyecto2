from unittest.util import _MAX_LENGTH
from django.db import models

class Persona(models.Model):
    nombre = models.CharField(max_lenght=30)
    apellido = models.CharField(max_lenght=30)
    edad = models.IntegerField()