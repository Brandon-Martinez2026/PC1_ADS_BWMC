# BWMC
# Tuplas
import pyfiglet
from rich.console import Console

# Texto
titulo = pyfiglet.figlet_format("Brandon")
from colorama import init, Fore, Style

init()
print(Fore.BLUE + titulo + Style.RESET_ALL)
console = Console()

#Creamos tupla con nombre de empelados
empleados_autorizados = ("brandon", "Paola", "motit", "chusit", "Carlos")

#Mensaje de bienvenida
print("Verificación de acceso al sistema")

#Solicitamos el nombre del usuario
nombre = input("Ingrese su nombre: ")

#verificar si el nombre esta en la tupla
if nombre in empleados_autorizados:
    #si esta damos acceso
    print(f"Bienvenido {nombre}, tienes acceso al sistema.")
else:
    #si no esta denegamos el acceso
    print(f"Lo siento no tienes acceso al sistema.")