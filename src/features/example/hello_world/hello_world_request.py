from dataclasses import dataclass


@dataclass(frozen=True)
class HelloWorldRequest:
    """Nombre opcional para personalizar el saludo."""

    name: str = ""
