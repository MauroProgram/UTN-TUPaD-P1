'''
Crea un programa que pida al usuario nombre, apellido, edad y residencia
'''

#Funciones
def informacion_personal(nombre,apellido,edad,residencia):
    return f"Hola {nombre} {apellido}, tienes {edad} años y vives en {residencia}." 

#Programa principal

nombre = input("Introduce tu nombre: ")
apellido = input("Introduce tu apellido: ")
edad = input("Introduce tu edad: ")
residencia = input("Introduce tu residencia: ")
informacion = informacion_personal(nombre,apellido,edad,residencia)
print(informacion)