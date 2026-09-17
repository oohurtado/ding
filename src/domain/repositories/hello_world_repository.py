from abc import ABC, abstractmethod

from domain.models.entities.hello_world import HelloWorld


class HelloWorldRepository(ABC):
    """Contrato independiente del almacenamiento concreto."""

    @abstractmethod
    def get_greeting(self) -> HelloWorld:
        """Obtiene la entidad del saludo."""
        raise NotImplementedError
