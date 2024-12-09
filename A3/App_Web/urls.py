from django.urls import path

from . import views

from .views import index, cadastro, novasenha, logado, usuarios

urlpatterns = [
    #path('', index),
    path('', views.index, name='index'),
    path('index', index),
    path('cadastro', cadastro),
    path('novasenha', novasenha),
    path('logado', logado),
    path('usuarios', usuarios),
    path('login/', views.login_view, name='login'),
]