from django.shortcuts import render
from .models import Pelicula

def home(request):
    latest = Pelicula.objects \
        .order_by('-anno')[:8]

    context = {
        "latest_movies": latest
    }

    return render(request, 'index.html', context)

