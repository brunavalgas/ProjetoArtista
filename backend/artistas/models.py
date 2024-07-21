from django.db import models

TIPO_ARTISTA = { # Enum
    "SOLO": "Solo", # Chave: SOLO, Valor: Solo
    "BANDA": "Banda" # Chave: BANDA, Valor: Banda
}

TIPO_DOCUMENTO = { # Enum
    "CPF": "CPF", # Chave: CPF, Valor: CPF
    "RG": "RG"  # Chave: RG, Valor: RG
}

class Documento(models.Model): # Classe Documento
    id = models.AutoField(primary_key=True) # Atributo id
    numero = models.CharField(max_length=100) # Atributo numero
    tipo = models.CharField(choices=TIPO_DOCUMENTO, max_length=100) # enum
    

class Artista(models.Model): # Classe Artista
    id = models.AutoField(primary_key=True) # Atributo id
    nome = models.CharField(max_length=100) # Atributo nome
    tipo = models.CharField(choices=TIPO_ARTISTA, max_length=100) # enum
    email = models.EmailField() # Atributo email
    documento = models.OneToOneField(Documento, on_delete=models.CASCADE) # Atributo documento

