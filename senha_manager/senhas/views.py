from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Senha
from django.contrib.auth.decorators import login_required
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

@login_required
def listar_senhas(request):
    senhas = Senha.objects.order_by('-criada_em')
    return render(request, 'senhas/listar_senhas.html', {'senhas': senhas})

@login_required
def chamar_senha(request, senha_id):
    senha = get_object_or_404(Senha, id=senha_id)
    senha.chamada = True
    senha.save()

    # Notificar via WebSocket
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        'senha_updates',
        {
            'type': 'send_update',
            'message': senha.numero
        }
    )

    messages.success(request, f"Senha {senha.numero} chamada com sucesso!")
    return redirect('listar_senhas')

@login_required
def senha_chamada(request):
    senha_atual = Senha.objects.filter(chamada=True).order_by('-criada_em').first()
    return render(request, 'senhas/senha_chamada.html', {'senha_atual': senha_atual})

@login_required
def gerar_senha(request):
    ultima_senha = Senha.objects.order_by('-numero').first()
    novo_numero = (ultima_senha.numero + 1) if ultima_senha else 1
    Senha.objects.create(numero=novo_numero)
    messages.success(request, f"Nova senha gerada: {novo_numero}")
    return redirect('listar_senhas')

@login_required
def resetar_senhas(request):
    Senha.objects.all().delete()
    messages.warning(request, "Todas as senhas foram resetadas.")
    return redirect('listar_senhas')

def interface_publica(request):
    return render(request, 'senhas/publico.html')