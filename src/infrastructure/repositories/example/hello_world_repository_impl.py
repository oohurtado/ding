from domain.models.example.hello_world_entity import HelloWorldEntity
from domain.repositories.example.hello_world_repository import HelloWorldRepository
from infrastructure.persistence.example.hello_world_memory import HelloWorldMemory


class HelloWorldRepositoryImpl(HelloWorldRepository):
    """Implementa el contrato y transforma datos en una entidad."""

    def __init__(self, storage: HelloWorldMemory) -> None:
        self._storage = storage

    def get_greeting(self) -> HelloWorldEntity:
        data = self._storage.read()
        return HelloWorldEntity(id=data["id"], message=data["message"])
