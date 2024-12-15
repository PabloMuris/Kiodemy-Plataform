from django.db import models

# Create your models here.


class Aula(models.Model):
    name = models.models.CharField(max_length=200)
    video = models.models.NullBooleanField()


class Module(models.Model):
    name = models.CharField(max_length=200)
    aula = None

class Course(models.Model):
    nome = models.models.CharField(max_length=200)
    descricao = models.models.CharField(max_length=200)
    modulo = None