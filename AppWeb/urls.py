from django.urls import path
from .views import *

urlpatterns = [
    path('formulario/', formulario, name="formulario"),
    path('vendedor/', vendedor, name="vendedor"),
    path('comprador/', comprador, name="comprador"),
    path('busquedaMail/', busquedaMail, name="busquedaMail"),
    path('buscar/', buscar, name="buscar"),
    path('registro/', registro, name="registro"),
    path('login/', login, name="login"),
    path('resultadosRegistro/', resultadosRegistro, name="resultadosRegistro"),
    path('eliminarRegistrado/<id>/', eliminarRegistrado, name="eliminarRegistrado"),
    path('editarRegistrado/<id>/', editarRegistrado, name="editarRegistrado"),
]
