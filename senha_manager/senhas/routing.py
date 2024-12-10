from django.urls import re_path
from .consumers import SenhaConsumer
from . import consumers

websocket_urlpatterns = [
    re_path(r'ws/senha/$', consumers.SenhaConsumer.as_asgi()),
]