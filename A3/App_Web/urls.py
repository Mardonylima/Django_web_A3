from django.urls import path

from .views import index, cadastro, novasenha,logado, usuarios

urlpatterns = [
    path('', index),
    path('index', index),
    path('cadastro', cadastro),
    path('novasenha', novasenha),
    path('logado', logado),
    path('usuarios', usuarios),
]