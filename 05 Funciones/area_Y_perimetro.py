'''Calcular area y perimetro de un circulo'''
#Import
import math
#Funciones
def area_ciruclo(radio):
    return math.pi * radio**2
def perimetro_circulo(radio):
    return 2 * math.pi * radio
#Programa principal
radio = float(input("Introduce el radio del circulo: "))
area = area_ciruclo(radio)
perimetro = perimetro_circulo(radio)    
print(f"El area del circulo es: {area}")
print(f"El perimetro del circulo es: {perimetro}")  
