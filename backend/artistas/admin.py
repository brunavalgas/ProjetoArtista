from django.contrib import admin
from .models import Artista, Documento 
# Register your models here.

admin.site.register(Artista) # Cadastramos o modelo Artista no admin
admin.site.register(Documento) # Cadastramos o modelo Documento no admin