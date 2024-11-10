from colorama import Fore, Back, Style, init

# Initialize colorama
init()

def print_colored(text, color="", background="", reset=Style.RESET_ALL):
    """
    Imprime texto con color personalizado.
    
    Parámetros:
    - text: Texto a imprimir.
    - color: Color del texto (de colorama.Fore).
    - background: Color del fondo (de colorama.Back).
    - reset: Estilo de reset para restablecer.
    """
    print(f"{color}{background}{text}{reset}")

# Colores y fondos
TEXT_RED = Fore.RED
TEXT_GREEN = Fore.GREEN
BACKGROUND_YELLOW = Back.YELLOW

# Usar la función
print_colored("Texto en rojo", color=TEXT_RED)
print_colored("Texto verde con fondo amarillo", color=TEXT_GREEN, background=BACKGROUND_YELLOW)


