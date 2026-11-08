from django.shortcuts import render
from .models import Pelicula, Director, Genero
from django.http import HttpResponse, HttpResponseBadRequest


def home(request):
    latest = Pelicula.objects \
        .order_by('-anno')[:8]

    context = {
        "latest_movies": latest
    }

    return render(request, 'index.html', context)

def lista_generos(request):
    generos = Genero.objects.all()
    nombre_genero = request.GET.get("genero")
    context = {
        "generos" : generos
    }
    if nombre_genero:
        genero_seleccionado = generos.filter(genero=nombre_genero).first()
        if genero_seleccionado:
            context["genero_seleccionado"] = genero_seleccionado
            context["peliculas"] = genero_seleccionado.pelicula_set.all()
    return render(request, 'generos.html', context)

def lista_directores(request):
    directores = Director.objects.all()
    context = {
        "directores" : directores
    }
    return render(request, 'directores.html', context)

def director_detalle(request, id_director):
    director = Director.objects.get(id=id_director)
    peliculas = Pelicula.objects.filter(director=director)
    context = {
        "director": director,
        "peliculas": peliculas
    }
    return render(request, 'director_detalles.html', context)




def get_peliculas(request):
    peliculas = Pelicula.objects.all()
    context={"peliculas":peliculas}
    return render(request, 'peliculas.html',context)


def detalle_pelicula(request, id_pelicula: int):
    pelicula = Pelicula.objects.get(pk = id_pelicula)
    context = {"pelicula" : pelicula}
    return render(request, 'detalle_pelicula.html', context)
