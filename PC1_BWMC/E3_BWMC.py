import pyfiglet

# Generar el texto en forma de arte ASCII
titulo = pyfiglet.figlet_format("INTELAF")
print(titulo)

# Texto
titulon = pyfiglet.figlet_format("Brandon")
from colorama import init, Fore, Style

init()
print(Fore.BLUE + titulon + Style.RESET_ALL)

# Tupla que contiene los salarios de los empleados
salarios = (5500, 6200, 4800, 7100, 5900)

# Inicializamos la suma total
total = 0

# Recorremos la tupla y
for salario in salarios:
    total += salario

# Sumamos cada salario

# Mostramos el total acumulado
print("\nml Total de salarios a pagar este mes: Q", total)
