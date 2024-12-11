from django.db import models

# Create your models here.
class Fila(models.Model):
    nome = models.CharField(max_length=100)  # Nome descritivo da fila
    id_usb = models.CharField(max_length=50, unique=True)  # ID USB único do teclado

    def __str__(self):
        return self.nome

class Senha(models.Model):
    numero = models.IntegerField(unique=True)
    chamada = models.BooleanField(default=False)
    criada_em = models.DateTimeField(auto_now_add=True)  # Nova coluna
    chamada_em = models.DateTimeField(null=True, blank=True)  # Nova coluna
    fila = models.ForeignKey(Fila, on_delete=models.CASCADE, default=1) # Use o ID de uma fila existente

    def __str__(self):
        return f"Senha {self.numero} ({self.fila.nome})"