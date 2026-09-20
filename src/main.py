from features.example.hello_world.hello_world_request import HelloWorldRequest
from dependencies import get_hello_world_handler
from infrastructure.config.model_registry import register_entities
from infrastructure.database.database import Base, engine
from presentation.routers.hello_world_router import hello_world_router


def main() -> None:
    register_entities()
    Base.metadata.create_all(bind=engine)
    request = HelloWorldRequest(name="Oliver")
    response = hello_world_router(get_hello_world_handler(), request)
    print(response.message)


if __name__ == "__main__":
    main()
