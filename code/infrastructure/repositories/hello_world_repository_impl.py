from code.domain.models.entities.hello_world import HelloWorld
from code.domain.repositories.hello_world_repository import HelloWorldRepository
from code.infrastructure.persistance.hello_world_memory import HelloWorldMemory


class HelloWorldRepositoryImpl(HelloWorldRepository):
    """Implementa el contrato y transforma datos en una entidad."""

    def __init__(self, storage: HelloWorldMemory) -> None:
        self._storage = storage

    def get_greeting(self) -> HelloWorld:
        data = self._storage.read()
        return HelloWorld(id=data["id"], message=data["message"])
