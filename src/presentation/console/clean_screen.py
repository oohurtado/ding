import subprocess


def clear_screen() -> None:
    subprocess.run("cls", shell=True, check=True)