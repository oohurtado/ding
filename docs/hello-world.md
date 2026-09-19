# Feature example: hello-world

Ejemplo por capas que conserva la salida de consola `hola mundo`.

## Estructura

```text
src/
├── domain/
│   ├── models/hello_world.py
│   └── repositories/hello_world_repository.py
├── features/
│   └── example/hello_world/
│       ├── use_case.py
│       └── dto.py
├── infrastructure/
│   ├── database/database.py
│   ├── repositories/hello_world_repository_impl.py
│   └── persistence/example/hello_world_memory.py
├── presentation/
│   ├── routers/example_router.py
│   └── schemas/hello_world_response.py
├── dependencies.py
└── main.py
```

El dominio contiene la entidad y el contrato del repositorio. El caso de uso
vive junto a su DTO en `features/example/hello_world` y depende del contrato.
La implementación convierte los datos del almacenamiento en memoria a la entidad.
`dependencies.py` ensambla estas dependencias mediante inyección por constructor.

La función `hello_world` de `example_router.py` recibe el caso de uso y convierte
su DTO al esquema de presentación. Es un adaptador de consola; no expone rutas
HTTP ni requiere un framework web. El saludo no recibe parámetros, por lo que
solo tiene un esquema de respuesta y no necesita un esquema de solicitud.

## Flujo

```text
main -> example_router.hello_world -> HelloWorldUseCase.execute
     -> HelloWorldRepository.get_greeting -> HelloWorldRepositoryImpl
     -> HelloWorldMemory.read
     <- entidad <- DTO <- esquema de presentación -> print
```

## Ejecutar

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
