# Ingrese el nombre del empleado para revisar su asistencia:
import pyfiglet
# Generar el texto en forma de arte ASCII
titulo = pyfiglet.figlet_format("INTELAF")
print(titulo)

# Texto
titulon = pyfiglet.figlet_format("Brandon")
from colorama import init, Fore, Style

init()
print(Fore.BLUE + titulon + Style.RESET_ALL)

# Definimos tuplas con los nombres de empleados presentes por dia
lunes = ("Ana", "Luis", "Carlos")
martes = ("Ana", "Sofia", "Luis")
miercoles = ("Carlos", "Luis", "Marta")
jueves = ("Ana", "Carlos", "Sofia")
viernes = ("Luis", "Marta", "Sofia")
# Solicitamos al usuario el nombre del empleado a revisar
nombre = input("\nIngrese el nombre del empleado: ")
# Inicializamos el contador de dias presente
presente = 0
# Verificamos si el empleado estuvo presente cada dia
if nombre in lunes:
    presente += 1   
if nombre in martes:
    presente += 1
if nombre in miercoles:
    presente += 1
if nombre in jueves:
    presente += 1
if nombre in viernes:
    presente += 1
# Mostramos cuantos dias asistio el empleado
print(f"{nombre} asistio {presente} dias esta semana.")
