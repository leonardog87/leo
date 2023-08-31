from django import forms
from django.db import models

class MailForm(forms.Form):
    email=forms.EmailField()

class VendedorForm(forms.Form):
    nombre=forms.CharField(max_length=20)
    apellido=forms.CharField(max_length=20)
    email=forms.EmailField()
    
class CompradorForm(forms.Form):
    nombre=forms.CharField(max_length=20)
    apellido=forms.CharField(max_length=20)
    email=forms.EmailField()

#

class RegistroForm(forms.Form):
    usuario=forms.CharField(max_length=30)
    nombre=forms.CharField(max_length=30)
    apellido=forms.CharField(max_length=30)
    email=forms.EmailField()
