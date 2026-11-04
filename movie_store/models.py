from django.db import models


class Pelicula(models.Model):
    """ Modelo de Pelicula """
    id=models.IntegerField(primary_key=True)
    nombre=models.CharField(max_length=50)
    anno=models.IntegerField()
    director=models.CharField(max_length=30)
    generos=models.CharField(max_length=70)
    poster=models.CharField(max_length=100)

    def __repr__(self):
        texto= f"{self.nombre} ({self.anno}) - {self.director}.\nGeneros:{self.generos}"
        return texto

class Director(models.Model):
    id=models.IntegerField(primary_key=True)
    nombre=models.CharField(max_length=20)
    apellido=models.CharField(max_length=25)
    nacimiento=models.DateField()
    pais=models.CharField(max_length=20)

    def __repr__(self):
        texto= f"{self.nombre} {self.apellido} - {self.nacimiento} ({self.pais})"
        return texto

class Genero(models.Model):
    id=models.IntegerField(primary_key=True)
    genero=models.CharField(15)

    def __repr__(self):
        texto=f"{self.genero} ({self.genero})"
        return texto