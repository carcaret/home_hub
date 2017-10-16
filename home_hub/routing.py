from channels.routing import include

channel_routing = [
    include('camera.routing.websocket_routing', path=r'^/camera/?'),
]
