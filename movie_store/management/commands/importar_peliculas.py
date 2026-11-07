
import csv
import ast
from pathlib import Path
from datetime import date

from django.conf import settings
from django.core.management.base import BaseCommand
from django.db import transaction

from movie_store.models import Pelicula, Director, Genero


class Command(BaseCommand):
    help = "Borra e importa todos los datos de los tres CSV"

    @transaction.atomic
    def handle(self, *args, **kwargs):

        ruta = Path(settings.BASE_DIR)

        archivo_peliculas = ruta / "peliculas_dataset.csv"
        archivo_generos = ruta / "generos.csv"
        archivo_directores = ruta / "directores.csv"

        for archivo in [
            archivo_peliculas,
            archivo_generos,
            archivo_directores
        ]:
            if not archivo.exists():
                raise FileNotFoundError(
                    f"No se encuentra el archivo: {archivo}"
                )

        Pelicula.objects.all().delete()
        Director.objects.all().delete()
        Genero.objects.all().delete()

        with open(archivo_generos, encoding="utf-8-sig", newline="") as f:
            lector = csv.DictReader(f)

            for fila in lector:
                Genero.objects.create(
                    id=int(fila["id"]),
                    genero=fila["genero"].strip()
                )

        self.stdout.write(
            self.style.SUCCESS(
                f"{Genero.objects.count()} géneros importados."
            )
        )

        directores = {}

        with open(archivo_directores, encoding="utf-8-sig", newline="") as f:
            lector = csv.DictReader(f)

            for fila in lector:
                director = Director.objects.create(
                    nombre=fila["nombre"].strip(),
                    apellido=fila["apellido"].strip(),
                    nacimiento=date.fromisoformat(
                        fila["nacimiento"].strip()
                    ),
                    pais=fila["pais"].strip()
                )

                nombre_completo = (
                    f"{director.nombre} {director.apellido}"
                )

                directores[nombre_completo] = director

        self.stdout.write(
            self.style.SUCCESS(
                f"{Director.objects.count()} directores importados."
            )
        )

        with open(archivo_peliculas, encoding="utf-8-sig", newline="") as f:
            lector = csv.DictReader(f)

            for fila in lector:

                pelicula = Pelicula.objects.create(
                    nombre=fila["titulo"].strip(),
                    anno=int(fila["anno"]),
                    poster=fila["link_al_poster"].strip()
                )

                nombres_directores = [
                    nombre.strip()
                    for nombre in fila["director"].split(",")
                ]

                for nombre in nombres_directores:
                    if nombre not in directores:
                        raise ValueError(
                            f"Director no encontrado: {nombre}. "
                            f"Película: {fila['titulo']}"
                        )

                    pelicula.director.add(directores[nombre])

                generos_ids = ast.literal_eval(fila["generos"])

                for genero_id in generos_ids:
                    try:
                        genero = Genero.objects.get(
                            id=int(genero_id)
                        )
                    except Genero.DoesNotExist:
                        raise ValueError(
                            f"Género no encontrado: {genero_id}. "
                            f"Película: {fila['titulo']}"
                        )

                    pelicula.generos.add(genero)

        self.stdout.write("")
        self.stdout.write(
            self.style.SUCCESS("¡Importación completada!")
        )

        self.stdout.write(f"Películas: {Pelicula.objects.count()}")
        self.stdout.write(f"Directores: {Director.objects.count()}")
        self.stdout.write(f"Géneros: {Genero.objects.count()}")
