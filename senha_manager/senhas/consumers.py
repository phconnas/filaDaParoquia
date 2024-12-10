import json
from channels.generic.websocket import AsyncWebsocketConsumer

class SenhaConsumer(AsyncWebsocketConsumer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.historico = []  # Inicialize o histórico para cada instância

    async def connect(self):
        await self.channel_layer.group_add('senha_updates', self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard('senha_updates', self.channel_name)

    async def send_update(self, event):
        senha_atual = event['message']  # Apenas o número atual é enviado diretamente

        # Se o histórico for maior ou igual a 10, remova o mais antigo
        if len(self.historico) >= 10:
            self.historico.pop(0)

        # Adiciona o número ao histórico
        self.historico.append(senha_atual)

        # Envia os dados no formato correto
        await self.send(text_data=json.dumps({
            'senha_atual': senha_atual,  # Número atual
            'historico': list(reversed(self.historico))  # Últimos números em ordem reversa
        }))

        print(json.dumps({
            'senha_atual': senha_atual,
            'historico': list(reversed(self.historico))
        }))