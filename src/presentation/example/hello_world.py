"""Presentación de la feature hello-world."""

from application.use_cases.example.hello_world import HelloWorldUseCase


def say_hi(use_case: HelloWorldUseCase) -> None:
    response = use_case.execute()
    print(response.message)
