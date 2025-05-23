#Funciones
def operaciones_basicas(a,b):
    suma =a+b
    resta =a-b
    multiplicacion =a*b
    division = a/b
    return suma,resta,multiplicacion,division
#Programa principal
numero1 = int(input("Ingresa el primer numero:"))
numero2 = int(input("Ingresa el segundo numero: "))
suma, resta, multiplicacion, division = operaciones_basicas(numero1, numero2)
print(f"Suma: {suma}")
print(f"Resta: {resta}")
print(f"Multiplicación: {multiplicacion}")
print(f"División: {division}")