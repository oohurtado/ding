from dataclasses import dataclass


@dataclass(frozen=True)
class HelloWorldResponse:
    """Respuesta pública de presentación, independiente del DTO del caso de uso."""

    message: str
