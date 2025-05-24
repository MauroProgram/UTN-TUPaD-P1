'''
Crea una función recursiva que calcule el factorial de un número. Luego, utiliza esa función para calcular y mostrar en pantalla el factorial de todos los números enteros entre 1 y el número que indique el usuario

'''
#Funciones
def factorial_recursivo (numero):
    if numero == 1:
        return 1
    else:
        return numero * factorial_recursivo(numero-1)

def mostrar_factorial (numero_limite):
    print(f"\nFactoriales de los números entre 1 y {numero_limite}:")
    for i in range (1,numero_limite +1):
        print(f"El factorial de {i} es: {factorial_recursivo(i)}")

def validar_numero(numero_usuario):
    if numero_usuario < 0:
        print("Por favor, ingresa un numero entero NO NEGATIVO")
    else:
        mostrar_factorial(numero_usuario)
#Programa Principal
numero = int(input("Hasta que numero desea calcular los factoriales. "))
validar_numero(numero)
