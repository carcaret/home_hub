from channels.routing import route

def message_handler(message):
    print(message['text'])

websocket_routing = [
    route("websocket.receive", message_handler),
]
