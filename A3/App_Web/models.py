from django.db import models

class Usuario(models.Model):
    nome = models.CharField(max_length=255)
    login = models.CharField(max_length=255)
    senha = models.CharField(max_length=255)

    class Meta:
        db_table = 'login'  # Nome da tabela já criada no banco

    def __str__(self):
        return self.nome
