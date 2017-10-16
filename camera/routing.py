import json
from channels import Group
from channels.routing import route

from .audio_socket import ws_connect

websocket_routing = [
    route("websocket.connect", ws_connect),
]

