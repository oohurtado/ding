class HelloWorldMemory:
    """Simula una lectura de almacenamiento sin base de datos."""

    def read(self) -> dict[str, str]:
        return {"id": "hello-world", "message": "hola mundo"}
