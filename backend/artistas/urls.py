from django.urls import path

from .import views

urlpatterns = [ # Lista de URLs
    path('create', views.create_artista, name='create_artista'), # URL para criar um artista
    path('read_artistas', views.read_artistas, name='read_artistas'), # URL para ler todos os artistas
    path('read_artistas/<int:id>', views.read_artistas_by_id, name='read_artista'), # URL para ler um artista por id
    path('delete_artista/<int:id>', views.delete_artista, name='delete_artista'), # URL para deletar um artista
]

