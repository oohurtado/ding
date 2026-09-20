from presentation.console.clean_screen import clear_screen
from presentation.console.example.hello_world_screen import user_input as user_input_example

def menu_init():
    while True:
        clear_screen()
        
        print("\n--- Menú principal ---")
        print("1. Ejecutar Hello World")
        print("0. Salir")

        print()
        option = input("Elige una opción: ").strip()
        print()
        print("*" * 50)
        print()

        match option:
            case "1":
                user_input_example()                

            case "0":
                print("Hasta luego")
                break

            case _:
                print("Opción inválida. Intenta de nuevo.")