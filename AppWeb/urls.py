from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('formulario/', formulario, name="formulario"),
    path('vendedor/', vendedor, name="vendedor"),
    path('comprador/', comprador, name="comprador"),
    path('busquedaMail/', busquedaMail, name="busquedaMail"),
    path('buscar/', buscar, name="buscar"),
    path('registro/', registro, name="registro"),
    path('resultadosRegistro/', resultadosRegistro, name="resultadosRegistro"),
    path('eliminarRegistrado/<id>/', eliminarRegistrado, name="eliminarRegistrado"),
    path('editarRegistrado/<id>/', editarRegistrado, name="editarRegistrado"),

#views    
    path('registroList/', RegistroList.as_view(), name="registroList"),
    path('registroDetail/<pk>', RegistroDetail.as_view(), name="registroDetail"),
    path('registroForm/nuevo/', RegistroCreate.as_view(), name="registroForm"),
    path('registroList/update/<pk>', RegistroUpdate.as_view(), name="registroUpdate"),
    path('registroList/delete/<pk>', RegistroDelete.as_view(), name="registroDelete"),

#login
    path('login/', login_request, name='login'),
    path('register/', register, name='register'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('editarPerfil/', editarPerfil, name='editarPerfil'),
    path('passwordCambio/', CambioPassword.as_view(), name='cambiar_password'),
    path('passwordExitoso/' , password_exitoso, name='password_exitoso'),
]
