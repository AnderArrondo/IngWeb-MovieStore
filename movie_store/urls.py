from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    # path('directores', views.lista_directores, name='directores'),
    # path('directores/<str:id_director>/', views.director_detalle, name='director_detalles'),
]