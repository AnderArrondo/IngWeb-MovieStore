from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),

    path("generos/", views.lista_generos, name="generos"),

    path("directores/", views.lista_directores, name="directores"),
    path("directores/<int:id_director>/", views.director_detalle, name="director_detalles"),
]