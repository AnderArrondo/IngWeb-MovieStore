from django.shortcuts import render
from .models import Pelicula
from .models import Director

def home(request):
    latest = Pelicula.objects \
        .order_by('-anno')[:8]

    context = {
        "latest_movies": latest
    }

    return render(request, 'index.html', context)

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


