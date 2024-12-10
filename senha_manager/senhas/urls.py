from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_senhas, name='listar_senhas'),
    path('chamar/<int:senha_id>/', views.chamar_senha, name='chamar_senha'),
    path('senha-chamada/', views.senha_chamada, name='senha_chamada'),
    path('gerar-senha/', views.gerar_senha, name='gerar_senha'),
    path('resetar-senhas/', views.resetar_senhas, name='resetar_senhas'),
    path('publico/', views.interface_publica, name='interface_publica'),
]