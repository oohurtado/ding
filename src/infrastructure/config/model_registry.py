"""Registro explícito de los módulos que contienen modelos SQLAlchemy."""

from importlib import import_module


MODEL_MODULES = (
    "domain.models.entities.user_entit",
)


def register_entities() -> None:
    """Carga los modelos para registrar sus tablas en Base.metadata."""
    for module_name in MODEL_MODULES:
        import_module(module_name)
