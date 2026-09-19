from dependencies import get_hello_world_use_case
from infrastructure.config.model_registry import register_entities
from infrastructure.database.database import Base, engine
from presentation.routers.example_router import hello_world


def main() -> None:
    register_entities()
    Base.metadata.create_all(bind=engine)
    response = hello_world(get_hello_world_use_case())
    print(response.message)


if __name__ == "__main__":
    main()
