from django.db import models

# Create your models here.
class Senha(models.Model):
    numero = models.IntegerField(unique=True)
    chamada = models.BooleanField(default=False)
    criada_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Senha {self.numero}"