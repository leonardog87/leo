from django.shortcuts import render
from django.http import HttpResponse
from .models import Mail, Vendedor, Comprador, Registro
from .forms import MailForm, CompradorForm, VendedorForm, RegistroForm

# Create your views here.

def inicio(request):
    return render(request,'AppWeb/inicio.html')

def formulario(request):
    formulario_mail=MailForm()
    if request.method=="POST":
        email=request.POST["email"]
        correo=Mail(email=email)
        correo.save()
        return render(request,'AppWeb/formulario.html' , {"formulario_mail": formulario_mail, "mensaje":"Gracias por suscribirte!"})
    else:
       return render(request,'AppWeb/formulario.html', {"formulario_mail": formulario_mail})
    
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

def busquedaMail(request):
    return render(request,'AppWeb/busquedaMail.html')

def buscar(request):
    email=request.GET["email"]
    if email!="":
        datos=Mail.objects.filter(email=email)
        return render(request,'AppWeb/resultadosBusqueda.html', {"datos": datos})
    else:        
        return render(request,'AppWeb/busquedaMail.html', {"mensaje_nobusqueda":"no buscaste nada!"})
        
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

def login(request):
    return render(request,'AppWeb/login.html')

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
