from django.shortcuts import render, redirect
from .models import Senha

def listar_senhas(request):
    senhas = Senha.objects.order_by('-criada_em')
    return render(request, 'senhas/listar_senhas.html', {'senhas': senhas})

def chamar_senha(request, senha_id):
    senha = Senha.objects.get(id=senha_id)
    senha.chamada = True
    senha.save()
    messages.success(request, f"Senha {senha.numero} chamada com sucesso!")
    return redirect('listar_senhas')

def senha_chamada(request):
    senha_atual = Senha.objects.filter(chamada=True).order_by('-criada_em').first()
    return render(request, 'senhas/senha_chamada.html', {'senha_atual': senha_atual})

def gerar_senha(request):
    ultima_senha = Senha.objects.order_by('-numero').first()
    novo_numero = (ultima_senha.numero + 1) if ultima_senha else 1
    Senha.objects.create(numero=novo_numero)
    messages.success(request, f"Nova senha gerada: {novo_numero}")
    return redirect('listar_senhas')

def resetar_senhas(request):
    Senha.objects.all().delete()
    messages.warning(request, "Todas as senhas foram resetadas.")
    return redirect('listar_senhas')
