from django.db import models


class Director(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    nacimiento = models.DateField(null=True, blank=True)
    pais = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


class Genero(models.Model):
    id = models.IntegerField(primary_key=True)
    genero = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.genero


class Pelicula(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    anno = models.IntegerField()
    director = models.ManyToManyField(Director)
    generos = models.ManyToManyField(Genero)
    poster = models.URLField(max_length=500)

    def __str__(self):
        return f"{self.nombre} ({self.anno})"