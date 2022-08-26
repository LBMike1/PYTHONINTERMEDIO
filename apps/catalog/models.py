from django.conf import settings
from django.db import models


class Catalogo(models.Model):
    nombre_catalogo = models.CharField(max_length=40)
    especie = models.CharField(max_length=20)
    genero = models.CharField(max_length=1)
