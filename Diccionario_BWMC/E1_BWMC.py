# Diccionario en Python
# BWMC
# Texto
import pyfiglet
titulon = pyfiglet.figlet_format("Brandon")
from colorama import init, Fore, Style

init()
print(Fore.BLUE + titulon + Style.RESET_ALL)

monedas = {'Euro':'€', 'Dollar':'$', 'Yen':'¥',"Quetzal":'Q'}
moneda = input("Introduce una divisa: ")
print(monedas.get(moneda.title(), "La divisa no está."))
