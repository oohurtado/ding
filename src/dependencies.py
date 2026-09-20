"""Ensamblado de las dependencias de la aplicación."""

from features.example.hello_world.hello_world_handler import HelloWorldHandler
from infrastructure.persistence.example.hello_world_memory import HelloWorldMemory
from infrastructure.repositories.hello_world_repository_impl import HelloWorldRepositoryImpl


def get_hello_world_handler() -> HelloWorldHandler:
    storage = HelloWorldMemory()
    repository = HelloWorldRepositoryImpl(storage)
    return HelloWorldHandler(repository)
