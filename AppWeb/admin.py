from django.contrib import admin

# Register your models here.

from .models import Mail, Vendedor, Comprador, Registro

admin.site.register(Mail)
admin.site.register(Vendedor)
admin.site.register(Comprador)
admin.site.register(Registro)