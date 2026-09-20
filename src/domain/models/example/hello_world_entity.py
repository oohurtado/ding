from dataclasses import dataclass


@dataclass(frozen=True)
class HelloWorldEntity:
    """Entidad que representa un saludo con identidad."""

    id: str
    message: str
