from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class AlunoUser(AbstractUser):
    SCHOLARITY_CHOICES = {
        'SR': 'Sem Resposta',
        'FI': 'Fundamental Incompleto',
        'SR': 'Fundamental Completo',
        'MI': 'Ensino Médio Incompleto',
        'MC': 'Ensino Médio Completo',
        'SI': 'Superior Incompleto',
        'SC': 'Superior Completo',
        'ME': "Mestrado",
        'DR': 'Doutorado',
        'ES': 'Especialização',

    }



    cpf = models.CharField(max_length=11)
    email = models.EmailField(max_length=254,unique=True)
    escolaridade = models.Choices(SCHOLARITY_CHOICES)
    phone = models.CharField(max_length=11)





class Professor(AlunoUser):
    nome = models.models.CharField(max_length=200)
    cursos = models.ManyToManyField()