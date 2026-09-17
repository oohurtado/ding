# Feature hello-world

Ejemplo educativo del recorrido entre capas DDD. Solo imprime `hola mundo`.
Requiere Python 3.9 o superior, sin dependencias externas ni base de datos.

## Ejecutar

Desde la raíz del repositorio `ding`:

```powershell
python -B -m src.presentation.hello_world
```

También puedes ejecutar el archivo directamente desde cualquier carpeta:

```powershell
python -B "C:\Users\OSCAR\Desktop\Dev\Code\ding\src\presentation\hello_world.py"
```

La entrada agrega la raíz del proyecto a la ruta de imports cuando se ejecuta
como archivo. Desde `src/presentation/hello_world.py`, `parents[2]` apunta a
`ding/`, la carpeta que contiene el paquete `src`.

Salida: `hola mundo`.

## Archivos y responsabilidades

Rutas relativas a `src/`:

| Archivo | Responsabilidad |
| --- | --- |
| `presentation/hello_world.py` | Ensambla e inyecta dependencias y muestra el resultado. |
| `application/use_cases/hello_world.py` | Orquesta el saludo mediante la interfaz y devuelve un DTO. |
| `domain/repositories/hello_world_repository.py` | Interfaz abstracta del repositorio. |
| `domain/models/entities/hello_world.py` | Entidad con identidad y mensaje. |
| `domain/models/dtos/hello_world_response.py` | Modelo de salida con el mensaje para el consumidor. |
| `infrastructure/repositories/hello_world_repository_impl.py` | Implementación que convierte datos en entidad. |
| `infrastructure/persistence/hello_world_memory.py` | Simula almacenamiento mediante datos fijos en memoria. |

## Flujo

```text
main()
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

El punto de entrada conoce las clases concretas y las inyecta por constructor.
El caso de uso solo conoce el contrato del repositorio. Infraestructura depende
del dominio para implementarlo; el dominio no depende de aplicación ni de
infraestructura. Otra implementación del contrato puede sustituir a la actual
cambiando su ensamblado en el punto de entrada.

Se conserva el nombre existente `persistence` y se coloca el DTO en
`domain/models/dtos`, siguiendo las carpetas originales. En otras estructuras
DDD, los DTO de salida pueden vivir en aplicación. La identidad del saludo es
solo didáctica; este ejemplo no tiene reglas de negocio complejas.

Los casos de uso viven en `application/use_cases` y la entrada en `presentation`.
La feature se llama `hello-world`, pero sus módulos usan `hello_world`
para poder importarlos en Python.
