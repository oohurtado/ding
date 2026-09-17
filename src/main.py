from dependencies import get_hello_world_use_case
from presentation.example.hello_world import say_hi


if __name__ == "__main__":
    use_case = get_hello_world_use_case()
    say_hi(use_case)
