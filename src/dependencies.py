"""Ensamblado de las dependencias de la aplicación."""

from application.use_cases.example.hello_world import HelloWorldUseCase
from infrastructure.persistence.example.hello_world_memory import HelloWorldMemory
from infrastructure.repositories.example.hello_world_repository_impl import (
    HelloWorldRepositoryImpl,
)


def get_hello_world_use_case() -> HelloWorldUseCase:
    storage = HelloWorldMemory()
    repository = HelloWorldRepositoryImpl(storage)
    useCase = HelloWorldUseCase(repository)
    return useCase
