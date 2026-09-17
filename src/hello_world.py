"""Punto de entrada y ensamblado de la feature hello-world."""

# Al ejecutar este archivo directamente, Python agrega code/ a sys.path.
# Agregamos su carpeta padre para resolver el paquete local code.
if __package__ in (None, ""):
    import sys
    from pathlib import Path

    sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from src.application.use_cases.hello_world import HelloWorldUseCase
from src.infrastructure.persistance.hello_world_memory import HelloWorldMemory
from src.infrastructure.repositories.hello_world_repository_impl import (
    HelloWorldRepositoryImpl,
)


def main() -> None:
    storage = HelloWorldMemory()
    repository = HelloWorldRepositoryImpl(storage)
    use_case = HelloWorldUseCase(repository)
    response = use_case.execute()
    print(response.message)


if __name__ == "__main__":
    main()
