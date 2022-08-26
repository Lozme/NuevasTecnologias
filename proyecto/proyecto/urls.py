from django.contrib import admin
from django.urls import path
#Se debe importar la ruta de la vista
from PaginaWeb.views import PaginaPrincipal,Noticias,Foro,GuiaGOW,GuiaFreeFire,Analisis

#Se debe agregar la ruta en la que se mostrará la vista
urlpatterns = [
    path('', PaginaPrincipal),
    path('Noticias/',Noticias),
    path('Foro/',Foro),
    path('Guias/',GuiaGOW),
    path('Analisis/',Analisis),
    path('Guias/Free-Fire',GuiaFreeFire)
]
