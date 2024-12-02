from django.urls import path

from .views import index, cadastro, novasenha

urlpatterns = [
    path('index', index),
    path('cadastro', cadastro),
    path('novasenha', novasenha)
]