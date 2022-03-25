from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, date

# Create your models here.
class Perfil(models.Model):
    nome_completo = models.CharField(max_length=50, null=True)
    data_de_nascimento = models.DateField(" Data de nascimento (dia/mês/ano)",auto_now_add=False, auto_now=False, blank=False, null=True)
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return "{}".format(self.nome_completo)


