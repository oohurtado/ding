from domain.models.dtos.example.hello_world_response import HelloWorldResponse
from domain.repositories.example.hello_world_repository import HelloWorldRepository


class HelloWorldUseCase:
    """Depende del contrato, sin conocer la implementación concreta."""

    def __init__(self, repository: HelloWorldRepository) -> None:
        self._repository = repository

    def execute(self) -> HelloWorldResponse:
        greeting = self._repository.get_greeting()
        return HelloWorldResponse(message=greeting.message)
