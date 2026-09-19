from features.example.hello_world.use_case import HelloWorldUseCase
from presentation.schemas.hello_world_response import HelloWorldResponse


def hello_world(use_case: HelloWorldUseCase) -> HelloWorldResponse:
    """Adapta el resultado del caso de uso a la salida de presentación."""
    response = use_case.execute()
    return HelloWorldResponse(message=response.message)
