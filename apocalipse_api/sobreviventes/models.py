from django.db import models
import random
import uuid


class Sobrevivente(models.Model):
    id = models.AutoField(primary_key=True)
    jogo_id = models.CharField(max_length=100)
    nome = models.CharField(max_length=100)
    idade = models.IntegerField()
    sexo = models.CharField(max_length=1)
    latitude = models.FloatField(default=random.uniform(-15, 15))
    longitude = models.FloatField(default=random.uniform(-15, 15))
    avistado_infectado = models.IntegerField(default=0)
    infectado = models.BooleanField(default=False)
    
    def __str__(self):
        return self.nome

class Inventario(models.Model):
    id = models.AutoField(primary_key=True)
    sobrevivente = models.OneToOneField(Sobrevivente, on_delete=models.CASCADE)
    agua = models.IntegerField(default=0)
    comida = models.IntegerField(default=0)
    medicamento = models.IntegerField(default=0)
    municao = models.IntegerField(default=0)
    outros_itens = models.CharField(max_length=500, blank=True)
    
    def __str__(self):
        return self.sobrevivente.nome