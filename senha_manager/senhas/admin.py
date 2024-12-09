from django.contrib import admin

# Register your models here.
from .models import Senha

@admin.register(Senha)
class SenhaAdmin(admin.ModelAdmin):
    list_display = ('numero', 'chamada', 'criada_em')
    list_filter = ('chamada',)