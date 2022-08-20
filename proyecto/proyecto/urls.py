from django.contrib import admin
from django.urls import path
#Se debe importar la ruta de la vista
from PaginaWeb.views import nombreVista

#Se debe agregar la ruta en la que se mostrará la vista
urlpatterns = [
    path('NombreRuta/', nombreVista),
]
