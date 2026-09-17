from dataclasses import dataclass


@dataclass(frozen=True)
class HelloWorld:
    """Entidad que representa un saludo con identidad."""

    id: str
    message: str
