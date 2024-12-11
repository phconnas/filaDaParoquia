from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Senha
from django.contrib.auth.decorators import login_required
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from django.db.models import Count

@login_required
def listar_senhas(request):
    senhas = Senha.objects.order_by('-criada_em')
    return render(request, 'senhas/listar_senhas.html', {'senhas': senhas})

@login_required
def chamar_senha(request, senha_id):
    senha = get_object_or_404(Senha, id=senha_id)
    senha.chamada = True
    senha.chamada_em = timezone.now()
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
def gerar_senha(request, fila_id):
    fila = get_object_or_404(Fila, id=fila_id)  # Garante que a fila existe
    ultima_senha = Senha.objects.filter(fila=fila).order_by('-numero').first()
    novo_numero = (ultima_senha.numero + 1) if ultima_senha else 1
    Senha.objects.create(numero=novo_numero, fila=fila)
    return redirect('listar_senhas', fila_id=fila.id)

@login_required
def resetar_senhas(request):
    Senha.objects.all().delete()
    messages.warning(request, "Todas as senhas foram resetadas.")
    return redirect('listar_senhas')

@login_required
def relatorios(request):
    total_senhas = Senha.objects.count()
    chamadas = Senha.objects.filter(chamada=True).count()
    nao_chamadas = total_senhas - chamadas

    senhas_por_dia = Senha.objects.extra({'dia': "date(criada_em)"}).values('dia').annotate(total=Count('id'))

    return render(request, 'senhas/relatorios.html', {
        'total_senhas': total_senhas,
        'chamadas': chamadas,
        'nao_chamadas': nao_chamadas,
        'senhas_por_dia': senhas_por_dia,
    })

def interface_publica(request):
    return render(request, 'senhas/publico.html')