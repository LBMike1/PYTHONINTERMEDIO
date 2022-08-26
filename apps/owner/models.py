from django.db import models

from django.db import models


class Owner(models.Model):
    nombre = models.CharField(max_length=40)
    edad = models.IntegerField(max_length=3)
    pais = models.CharField(max_length=20, default='')

    def __str__(self):
        return "{} tiene {} años".format(self.nombre, self.edad)

