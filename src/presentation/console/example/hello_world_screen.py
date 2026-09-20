from features.example.hello_world.hello_world_request import HelloWorldRequest
from dependencies import get_hello_world_handler
from presentation.routers.hello_world_router import hello_world_router
from presentation.console.press_any_key import press_any_key


def user_input():
    name = input("Nombre (Enter para omitir): ")
    request = HelloWorldRequest(name=name)
    response = hello_world_router(get_hello_world_handler(), request)
    print(response.message)
    press_any_key()