"""Punto de entrada y ensamblado de la feature hello-world."""

from src.application.use_cases.hello_world import HelloWorldUseCase
from src.infrastructure.persistence.hello_world_memory import HelloWorldMemory
from src.infrastructure.repositories.hello_world_repository_impl import (
    HelloWorldRepositoryImpl,
)

def say_hi() -> None:
    storage = HelloWorldMemory()
    repository = HelloWorldRepositoryImpl(storage)
    use_case = HelloWorldUseCase(repository)
    response = use_case.execute()
    print(response.message)

