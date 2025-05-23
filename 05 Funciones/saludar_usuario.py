'''
Crear una funcion llamada saludar_usuario que reciba como parametro un nombre y devuelva un saludo personalizado.
'''

#Funciones
def saludar_usuario(nombre):
    return f"Hola {nombre}, bienvenido a la UTN!"
#Programa principal
nombre = input("Introduce tu nombre: ")
saludar = saludar_usuario(nombre)
print(saludar)
