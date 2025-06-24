'''
4) Escribí un programa que permita almacenar y consultar números telefónicos.
• Permití al usuario cargar 5 contactos con su nombre como clave y número como valor.
• Luego, pedí un nombre y mostrale el número asociado, si existe.

'''

contactos = {}

for i in range(5):
    nombre = input("Ingrese el nombre del contacto: ")
    numero = input("Ingrese el número telefónico: ")
    contactos[nombre] = numero

nombre_buscado = input("Ingrese el nombre del contacto a buscar: ")

if nombre_buscado in contactos:
    print("El número telefónico de", nombre_buscado, "es:", contactos[nombre_buscado])
else:
    print("Contacto no encontrado.")