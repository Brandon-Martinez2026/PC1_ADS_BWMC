# Diccionario en Python
# BWMC

nombre = input("¿Como te llamas? ")
edad = input("¿Cuantos años tienes? ")
clave = input("¿Cual es tu clave? ")
direccion = input("¿Cuál es tu dirección? ")
telefono = input("¿Cuál es tu número de teléfono? ")
#agregar datos a la tupla
persona = {"nombre": nombre, "edad": edad, "clave": clave, "direccion": direccion, "telefono": telefono}
print(
    persona["nombre"],
    "tiene",
    persona["edad"],
    "anos, su clave es",
    persona["clave"],
    ", vive en",
    persona["direccion"],
    "y su numero de telefono es",
    persona["telefono"],
)
