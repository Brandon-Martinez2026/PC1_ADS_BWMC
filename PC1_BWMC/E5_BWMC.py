# BWMC
# Tuplas en Python
import pyfiglet
# Generar el texto en forma de arte ASCII
titulo = pyfiglet.figlet_format("INTELAF")
print(titulo)

# Texto
titulon = pyfiglet.figlet_format("Brandon")
from colorama import init, Fore, Style

init()
print(Fore.BLUE + titulon + Style.RESET_ALL)

# Tupla que contiene las opciones del menú como pares (código, descripción)
menu_soporte = (
    ("1", "📋  Ver tickets abiertos"),
    ("2", "✅  Registrar nuevo ticket"),
    ("3", "🔒  Cerrar ticket"),
    ("4", "👋  Salir del sistema"),
)

# Titulo del sistema
print("\n Menú de Soporte Técnico")

# Mostramos cada opción usando un ciclo
for codigo, descripcion in menu_soporte:
    print(f"{codigo}. {descripcion}")

    # Iniciamos un bucle para que el usuario interactúe
while True:
    #Solicitamos una opción
    opcion = input("Seleccione una opción (1-4): ")

    # Evaluamos cada opción usando condicionales
    if opcion == "1":
        print(" 📋  Mostrando tickets abiertos ... ")
    elif opcion == "2":
        print(" ✅ Iniciando registro de nuevo ticket...")
    elif opcion == "3":
        print("🔒  Ticket cerrado")
    elif opcion == "4":
        print("👋  Saliendo del sistema. ¡Gracias!")
        # Salimos del bucle
        break
    else:
        print("Opcion invalida")
