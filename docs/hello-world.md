# Feature example: hello-world

Ejemplo por capas que recibe un request con un nombre opcional y devuelve un saludo.

## Estructura

```text
src/
├── domain/
│   ├── models/hello_world.py
│   └── repositories/hello_world_repository.py
├── features/
│   └── example/hello_world/
│       ├── hello_world_handler.py
│       ├── hello_world_request.py
│       └── hello_world_response.py
├── infrastructure/
│   ├── database/database.py
│   ├── repositories/hello_world_repository_impl.py
│   └── persistence/example/hello_world_memory.py
├── presentation/
│   └── routers/hello_world_router.py
├── dependencies.py
└── main.py
```

El dominio contiene la entidad y el contrato del repositorio. El caso de uso
vive junto a su respuesta en `features/example/hello_world` y depende del contrato.
La implementación convierte los datos del almacenamiento en memoria a la entidad.
`dependencies.py` ensambla estas dependencias mediante inyección por constructor.

La función `hello_world` de `hello_world_router.py` recibe el caso de uso y devuelve directamente su respuesta, definida en el feature. Es un adaptador de consola; no expone rutas
HTTP ni requiere un framework web. El request `HelloWorldRequest` contiene `name: str = ""`. Con un nombre devuelve
`hello <nombre>`; si está vacío o solo contiene espacios, devuelve `hello world`.

## Flujo

```text
main -> hello_world_router.hello_world -> HelloWorldHandler.execute
     -> HelloWorldRepository.get_greeting -> HelloWorldRepositoryImpl
     -> HelloWorldMemory.read
     <- entidad <- respuesta del feature -> print
```

## Ejecutar

Edita el request en `src/main.py`: `HelloWorldRequest(name="Oscar")` devuelve `hello Oscar`; `HelloWorldRequest()` o `HelloWorldRequest(name="")` devuelve `hello world`.

Desde la raíz del repositorio:

```powershell
python -B src/main.py
```

Se conservan los imports desde `src` (sin prefijo `src`); también funciona pasar
la ruta absoluta de `main.py`. No se usa `python -m src.main`.

El arranque conserva el registro de entidades SQLAlchemy y la creación de tablas
existentes. Por ello necesita SQLAlchemy, pydantic-settings, el controlador de la
base de datos y una conexión válida, además de las variables configuradas en
`src/.env`. El ejemplo en memoria, por sí solo, usa únicamente la biblioteca
estándar de Python y no accede a la base de datos.

La configuración de conexión vive ahora en `infrastructure/database/database.py`.
La entidad de usuario existente conserva su ubicación y usa esa nueva ruta.
