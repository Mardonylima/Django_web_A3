from django.db import models

class Usuario(models.Model):
    login = models.CharField(max_length=25, primary_key=True)  # Coluna 'login' em vez de 'usuario'
    nome = models.CharField(max_length=100)
    senha = models.CharField(max_length=25)

    def __str__(self):
        return self.usuario
