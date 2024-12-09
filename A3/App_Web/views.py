from django.shortcuts import render, redirect
from .models import Usuario
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

def index(request):
    return render(request, 'index.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['login']  # Nome de usuário
        password = request.POST['senha']  # Senha

        # Autenticando o usuário
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # Se o usuário for autenticado, faz o login
            login(request, user)
            return redirect('logado')  # Redireciona para a página de sucesso após o login
        else:
            # Se não conseguir autenticar, exibe uma mensagem de erro
            messages.error(request, 'Usuário ou senha inválidos.')
            return redirect('index')  # Redireciona de volta para a página de login
    else:
        return render(request, 'index.html')


def cadastro(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        username = request.POST.get('login')  # Nome de usuário
        password = request.POST.get('senha')  # Senha

        # Usando o método create_user para garantir que a senha será criptografada
        User.objects.create_user(username=username, password=password, first_name=nome)

        return redirect('index')  # Redireciona para a página de login
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
