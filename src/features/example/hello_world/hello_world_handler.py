from features.example.hello_world.hello_world_request import HelloWorldRequest
from features.example.hello_world.hello_world_response import HelloWorldResponse
from domain.repositories.hello_world_repository import HelloWorldRepository


class HelloWorldHandler:
    """Depende del contrato, sin conocer la implementación concreta."""

    def __init__(self, repository: HelloWorldRepository) -> None:
        self._repository = repository

    def execute(self, request: HelloWorldRequest) -> HelloWorldResponse:
        name = request.name.strip()
        if name:
            return HelloWorldResponse(message=f"hello {name}")
        greeting = self._repository.get_greeting()
        return HelloWorldResponse(message=greeting.message)
