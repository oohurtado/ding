from features.example.hello_world.hello_world_request import HelloWorldRequest
from features.example.hello_world.hello_world_handler import HelloWorldHandler
from features.example.hello_world.hello_world_response import HelloWorldResponse


def hello_world_router(handler: HelloWorldHandler, request: HelloWorldRequest) -> HelloWorldResponse:
    """Entrega el request al caso de uso y devuelve su respuesta."""
    return handler.execute(request)
