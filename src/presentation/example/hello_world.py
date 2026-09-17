"""Presentación y ensamblado de la feature hello-world."""

from application.use_cases.example.hello_world import HelloWorldUseCase
from infrastructure.persistence.example.hello_world_memory import HelloWorldMemory
from infrastructure.repositories.example.hello_world_repository_impl import (
    HelloWorldRepositoryImpl,
)


def say_hi() -> None:
    storage = HelloWorldMemory()
    repository = HelloWorldRepositoryImpl(storage)
    use_case = HelloWorldUseCase(repository)
    response = use_case.execute()
    print(response.message)
