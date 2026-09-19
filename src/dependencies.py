"""Ensamblado de las dependencias de la aplicación."""

from features.example.hello_world.use_case import HelloWorldUseCase
from infrastructure.persistence.example.hello_world_memory import HelloWorldMemory
from infrastructure.repositories.hello_world_repository_impl import HelloWorldRepositoryImpl


def get_hello_world_use_case() -> HelloWorldUseCase:
    storage = HelloWorldMemory()
    repository = HelloWorldRepositoryImpl(storage)
    return HelloWorldUseCase(repository)
