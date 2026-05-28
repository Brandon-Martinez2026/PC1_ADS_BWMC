# BWMC
# Tuplas en Python

import pyfiglet

# Generar el texto en forma de arte ASCII
titulo = pyfiglet.figlet_format("Intelaf")

print(titulo)
from rich.console import Console

# Texto
titulon = pyfiglet.figlet_format("Brandon")
from colorama import init, Fore, Style

init()
print(Fore.BLUE + titulo + Style.RESET_ALL)
console = Console()


# Creamos una tupla de tuplas, cada una con nombre y precio de producto
productos = (("Laptop", 6500), ("Monitor", 1800), ("Teclado", 250), ("Mouse", 120), ("Impresora", 900), ("Auriculares", 300), ("Webcam", 450), ("Disco Duro", 800), ("Memoria RAM", 600), ("Tarjeta Gráfica", 2000))

# Mostramos titulo del listado
print("\nLista de productos tecnológicos disponibles:")

# Recorremos la tupla principal con un ciclo
for producto, precio in productos:
# Imprimimos cada producto con su precio formateado
    print(f"- {producto}: Q{precio}")   
