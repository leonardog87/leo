from django.shortcuts import render
from django.http import HttpResponse
from .models import Mail, Vendedor, Comprador, Registro
from .forms import MailForm, CompradorForm, VendedorForm, RegistroForm, RegisterUserForm, UserEditForm, FormularioCambioPassword
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from django.contrib.auth.mixins import LoginRequiredMixin #para vistas basadas en clases CLASS   
from django.contrib.auth.decorators import login_required #para vistas basadas en funciones DEF
from django.contrib.auth.views import LoginView, PasswordChangeView

@login_required
def formulario(request):
    formulario_mail=MailForm()
    if request.method=="POST":
        email=request.POST["email"]
        correo=Mail(email=email)
        correo.save()
        return render(request,'AppWeb/formulario.html' , {"formulario_mail": formulario_mail, "mensaje":"Gracias por suscribirte!"})
    else:
       return render(request,'AppWeb/formulario.html', {"formulario_mail": formulario_mail})

@login_required    
def comprador(request):
    formulario_comprador=CompradorForm()
    if request.method=="POST":
        nombre=request.POST["nombre"]
        apellido=request.POST["apellido"]
        email=request.POST["email"]
        datos_comprador=Comprador(nombre=nombre,apellido=apellido,email=email)
        datos_comprador.save()
        return render(request,'AppWeb/comprador.html', {"formulario_comprador": formulario_comprador, "mensaje_comprador":"comprador creado"})
    else:        
        return render(request,'AppWeb/comprador.html', {"formulario_comprador": formulario_comprador})

@login_required
def vendedor(request):
    formulario_vendedor=VendedorForm()
    if request.method=="POST":
        nombre=request.POST["nombre"]
        apellido=request.POST["apellido"]
        email=request.POST["email"]
        datos_vendedor=Vendedor(nombre=nombre,apellido=apellido,email=email)
        datos_vendedor.save()
        return render(request,'AppWeb/vendedor.html', {"formulario_vendedor": formulario_vendedor, "mensaje_vendedor":"vendedor creado"})
    else:
        return render(request,'AppWeb/vendedor.html', {"formulario_vendedor": formulario_vendedor})

@login_required
def busquedaMail(request):
    return render(request,'AppWeb/busquedaMail.html')


def buscar(request):
    email=request.GET["email"]
    if email!="":
        datos=Mail.objects.filter(email=email)
        return render(request,'AppWeb/resultadosBusqueda.html', {"datos": datos})
    else:        
        return render(request,'AppWeb/busquedaMail.html', {"mensaje_nobusqueda":"no buscaste nada!"})

@login_required        
def registro(request):
    formulario_registro=RegistroForm()
    if request.method=="POST":
        usuario=request.POST["usuario"]
        nombre=request.POST["nombre"]
        apellido=request.POST["apellido"]
        email=request.POST["email"]
        datos_registro=Registro(usuario=usuario,nombre=nombre,apellido=apellido,email=email)
        datos_registro.save()
        return render(request,'AppWeb/registro.html', {"formulario_registro": formulario_registro})
    else:
        return render(request,'AppWeb/registro.html', {"formulario_registro": formulario_registro})

#def login(request):
    return render(request,'AppWeb/login.html')

@login_required
def resultadosRegistro(request):
    registrados=Registro.objects.all()
    contexto={"registrados":registrados}
    return render(request,'AppWeb/resultadosRegistro.html', contexto)

def eliminarRegistrado(request,id):
    registro=Registro.objects.get(id=id)
    registro.delete()
    registrados=Registro.objects.all()
    contexto={"registrados": registrados}
    return render(request,'AppWeb/resultadosRegistro.html', contexto)

def editarRegistrado(request,id):
    registro=Registro.objects.get(id=id)
    if request.method=="POST":
        miFormulario=RegistroForm(request.POST)
        if miFormulario.is_valid():
            informacion=miFormulario.cleaned_data
            registro.usuario=informacion['usuario']
            registro.nombre=informacion['nombre']
            registro.apellido=informacion['apellido']
            registro.email=informacion['email']
            registro.save()
            registrados=Registro.objects.all()
            formulario_registro=RegistroForm()
            return render(request,'AppWeb/resultadosRegistro.html', {"formulario":formulario_registro, "registrados":registrados})
    else:
        formulario_registro=RegistroForm(initial={"usuario": registro.usuario, "nombre": registro.nombre, "apellido": registro.apellido, "email": registro.email})
        return render(request,'AppWeb/editarRegistrado.html', {"formulario": formulario_registro, "registro": registro})

class RegistroList(ListView):
    model=Registro
    template_name='AppWeb/registroList.html'

class RegistroDetail(DetailView):
    model=Registro
    template_name='AppWeb/registroDetail.html'

class RegistroCreate(CreateView):
    model=Registro
    success_url=reverse_lazy("inicio")
    fields=['usuario', 'nombre', 'apellido', 'email']

class RegistroUpdate(UpdateView):
    model=Registro
    success_url=reverse_lazy("inicio")
    fields=['usuario', 'nombre', 'apellido', 'email']

class RegistroDelete(DeleteView):
    model=Registro
    success_url=reverse_lazy("inicio")

def login_request(request):
    if request.method=="POST":
        form=AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            info=form.cleaned_data
            usu=info["username"]
            clave=info["password"]
            usuario=authenticate(username=usu, password=clave)#verifica si el usuario y la contraseña  existen
            if usuario is not None:#si el usuario no es None
                login(request, usuario)
                return render(request, "AppWeb/inicio.html", {"mensaje":f"Usuario {usu} logueado correctamente"})
            else:
                return render(request,"AppWeb/login.html", {"form":form, "mensaje":"Datos invalidos"})
        else:
            return render(request,"AppWeb/login.html", {"form":form, "mensaje":"Datos invalidos"})
    else:
        form=AuthenticationForm()
        return render(request,"AppWeb/login.html", {"form":form})
    
def register(request):
    if request.method=="POST":
        form=RegisterUserForm(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            nombre_usuario=info["username"]
            form.save()#grabo usuario en base de datos
            return render(request, "AppWeb/inicio.html", {"mensaje":f"Usuario {nombre_usuario} creado correctamente"})
        else:
            return render(request,"AppWeb/register.html", {"form":form, "mensaje":"Datos invalidos"})
    else:
        form=RegisterUserForm()
        return render(request,"AppWeb/register.html", {"form":form})
    
   
def inicio(request):
    return render(request,'AppWeb/inicio.html')

#@login_required
#def editarPerfil(request):
    usuario=request.user
    if request.method=="POST":
        form=UserEditForm(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            usuario.email=info["email"]
            usuario.password1=info["password1"]
            usuario.password2=info["password2"]
            usuario.first_name=info["first_name"]
            usuario.last_name=info["last_name"]
            usuario.save()
            return render(request, "AppWeb/inicio.html", {"mensaje":f"Usuario {usuario.username} editado correctamente"})
        else:
            return render(request, "AppWeb/editarPerfil.html", {"form": form, "nombreusuario":usuario.username, "mensaje":"Datos invalidos"})
    else:
        form=UserEditForm(instance=usuario)
        return render(request, "AppWeb/editarPerfil.html", {"form": form, "nombreusuario":usuario.username})
    
def editarPerfil(request):
    usuario=request.user
    if request.method=="POST":
        form=UserEditForm(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            usuario.email=info["email"]
            usuario.first_name=info["first_name"]
            usuario.last_name=info["last_name"]
            usuario.save()
            return render(request, "AppWeb/inicio.html", {"mensaje":f"Usuario {usuario.username} editado correctamente"})
        else:
            return render(request, "AppWeb/editarPerfil.html", {"form": form, "nombreusuario":usuario.username, "mensaje":"Datos invalidos"})
    else:
        form=UserEditForm(instance=usuario)
        return render(request, "AppWeb/editarPerfil.html", {"form": form, "nombreusuario":usuario.username})

class CambioPassword(PasswordChangeView):
    form_class = FormularioCambioPassword
    template_name = 'AppWeb/passwordCambio.html'
    success_url = reverse_lazy('password_exitoso')

def password_exitoso(request):
    return render(request, 'appWeb/passwordExitoso.html', {})