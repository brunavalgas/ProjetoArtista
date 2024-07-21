from django.core import serializers
from django.http import HttpResponse
from .models import Artista, Documento
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt # Decorator para desabilitar o CSRF
def create_artista(request): # Função para criar um artista
    nome = request.POST.get('nome_artista') # Pegamos o nome do artista
    tipo = request.POST.get('tipo_artista') # Pegamos o tipo do artista
    email = request.POST.get('email_artista') # Pegamos o email do artista

    numero_documento = request.POST.get('numero_documento') # Pegamos o número do documento
    tipo_documento = request.POST.get('tipo_documento') # Pegamos o tipo do documento

    doc = Documento.objects.create( # Criamos um documento
        numero=numero_documento,     
        tipo=tipo_documento     
    )
    
    Artista.objects.create( # Criamos um artista
        nome=nome,    
        tipo=tipo, 
        email=email,
        documento = doc
    )

    return HttpResponse('Artista criado com sucesso!') # Retornamos uma mensagem de sucesso

@csrf_exempt # Decorator para desabilitar o CSRF
def read_artistas(request): # Função para ler todos os artistas
    artista = Artista.objects.all() # Pegamos todos os artistas
    response = serializers.serialize('json', artista) # Serializamos os artistas
    return HttpResponse(response, content_type='application/json') # Retornamos os artistas em formato JSON

@csrf_exempt # Decorator para desabilitar o CSRF
def read_artistas_by_id(request, id): # Função para ler um artista por id
    artista = Artista.objects.filter(pk=id) # Pegamos o artista pelo id
    response = serializers.serialize('json', artista) # Serializamos o artista
    return HttpResponse(response, content_type='application/json') # Retornamos o artista em formato JSON

@csrf_exempt # Decorator para desabilitar o CSRF
def delete_artista(request, id): # Função para deletar um artista
    artista = Artista.objects.get(pk=id) # Pegamos o artista pelo id
    artista.delete() # Deletamos o artista
    return HttpResponse('Artista deletado com sucesso!') # Retornamos uma mensagem de sucesso