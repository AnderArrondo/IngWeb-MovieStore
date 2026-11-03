from django.db import models


class Pelicula(models.Model):
    """ Modelo de Pelicula """
    nombre=models.CharField(max_length=50)
    año=models.IntegerField()
    director=models.CharField(max_length=30)
    generos=models.CharField(max_length=70)
    poster=models.CharField(max_length=100)

    def __str__(self):
        texto=""" {} ({}) - {}.\nGeneros:{}""".format(self.nombre,self.año,self.director,self.generos)
        return texto