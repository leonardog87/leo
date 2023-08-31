from django.db import models

# Create your models here.

class Comprador(models.Model):
    nombre=models.CharField(max_length=20)
    apellido=models.CharField(max_length=20)
    email=models.EmailField()
    def __str__(self):
        return f"{self.nombre} - {self.apellido} - {self.email}"
   
class Mail(models.Model):
    email=models.EmailField()
    def __str__(self):
        return f"{self.email}"

class Vendedor(models.Model):
    nombre=models.CharField(max_length=20)
    apellido=models.CharField(max_length=20)
    email=models.EmailField()
    def __str__(self):
        return f"{self.nombre} - {self.apellido} - {self.email}"

class Registro(models.Model):
    usuario=models.CharField(max_length=30)
    nombre=models.CharField(max_length=30)
    apellido=models.CharField(max_length=30)
    email=models.EmailField()
    def __str__(self):
        return f"{self.usuario} - {self.nombre} - {self.apellido} - {self.email}"