from dataclasses import dataclass


@dataclass(frozen=True)
class HelloWorldResponse:
    """Datos de salida del caso de uso."""

    message: str
