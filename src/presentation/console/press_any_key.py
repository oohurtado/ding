import msvcrt


def press_any_key() -> None:
    print("\nPresiona cualquier tecla para continuar...", end="", flush=True)
    key = msvcrt.getwch()
    if key in ("\x00", "\xe0"):
        msvcrt.getwch()  # Consume el código extra de teclas como las flechas.
    print()