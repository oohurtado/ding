from abc import ABC, abstractmethod

from domain.models.example.hello_world_entity import HelloWorldEntity


class HelloWorldRepository(ABC):
    """Contrato independiente del almacenamiento concreto."""

    @abstractmethod
    def get_greeting(self) -> HelloWorldEntity:
        """Obtiene la entidad del saludo."""
        raise NotImplementedError
