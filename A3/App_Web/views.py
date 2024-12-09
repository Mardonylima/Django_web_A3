from django.shortcuts import render

from .models import Usuario
# Create your views here.

def index(request):
    return render(request, 'index.html')


def cadastro(request):
    return render(request, 'cadastro.html')


def novasenha(request):
    return render(request, 'novasenha.html')


def logado(request):
    return render(request, 'logado.html')

def usuarios(request):
    try:
        todos_usuarios = Usuario.objects.all()
    except Exception as e:
        todos_usuarios = []
        print(f"Erro ao buscar usuários: {e}")
    return render(request, 'usuarios.html', {'usuarios': todos_usuarios})