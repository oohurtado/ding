# Feature hello-world

Ejemplo educativo del recorrido entre capas DDD. Solo imprime `hola mundo`.
Requiere Python 3.9 o superior, sin dependencias externas ni base de datos.

## Ejecutar

Desde la raíz del repositorio `ding`:

```powershell
python -B src/main.py
```

También puedes ejecutar `src/main.py` por ruta absoluta desde otra carpeta.
No recibe parámetros. Salida: `hola mundo`.

`main.py` permanece dentro de `src`. Al ejecutarlo directamente, Python incluye
su carpeta en la búsqueda de módulos. Los imports comienzan con `application`,
`domain`, `infrastructure` o `presentation`, sin el prefijo `src` y sin modificar
`sys.path`. Este esquema usa `python src/main.py`, no `python -m src.main`.

## Archivos y responsabilidades

Rutas relativas a `src/`:

| Archivo | Responsabilidad |
| --- | --- |
| `main.py` | Obtiene el caso de uso de la fábrica y lo inyecta en `say_hi(use_case)`. |
| `dependencies.py` | Construye el almacenamiento, el repositorio concreto y el caso de uso. |
| `presentation/example/hello_world.py` | Recibe el caso de uso y muestra el resultado. |
| `application/use_cases/example/hello_world.py` | Orquesta el saludo mediante la interfaz y devuelve un DTO. |
| `domain/repositories/example/hello_world_repository.py` | Interfaz abstracta del repositorio. |
| `domain/models/entities/example/hello_world.py` | Entidad con identidad y mensaje. |
| `domain/models/dtos/example/hello_world_response.py` | Modelo de salida con el mensaje para el consumidor. |
| `infrastructure/repositories/example/hello_world_repository_impl.py` | Implementación que convierte datos en entidad. |
| `infrastructure/persistence/example/hello_world_memory.py` | Simula almacenamiento mediante datos fijos en memoria. |

## Flujo

```text
main.py
  -> get_hello_world_use_case() [ensambla almacenamiento, repositorio y caso de uso]
  -> say_hi(use_case)
  -> HelloWorldUseCase.execute()
     -> HelloWorldRepository.get_greeting() [interfaz]
        -> HelloWorldRepositoryImpl.get_greeting() [implementación inyectada]
           -> HelloWorldMemory.read()
           <- dict con id y message
        <- entidad HelloWorld
     <- DTO HelloWorldResponse
  -> print(response.message)
  -> hola mundo
```

`dependencies.py` conoce las clases concretas y las inyecta por constructor.
`main.py` entrega el caso de uso a presentación, que no construye repositorios.
La fábrica crea instancias nuevas en cada llamada, sin un contenedor externo.
El caso de uso solo conoce el contrato del repositorio. Infraestructura depende
del dominio para implementarlo; el dominio no depende de aplicación ni de
infraestructura. Otra implementación del contrato puede sustituir a la actual
cambiando su ensamblado en `dependencies.py`.

El DTO se conserva en `domain/models/dtos`, siguiendo la estructura original.
En otras estructuras DDD, los DTO de salida pueden vivir en aplicación.
La identidad del saludo es solo didáctica; este ejemplo no tiene reglas de
negocio complejas. Los módulos usan `hello_world` para poder importarlos.
