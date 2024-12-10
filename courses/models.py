from django.db import models

# Create your models here.

class Course(models.Model):
    nome = models.models.CharField(max_length=200)
    criador_por = models.ForeignKey