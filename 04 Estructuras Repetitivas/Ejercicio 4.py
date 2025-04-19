'''
4) Elabora un programa que permita al usuario ingresar números enteros y los sume en
secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese
un 0.

'''

num = int(input("Ingrese un número entero (0 para salir): "))
# Inicializar la variable suma
suma = 0
# Utilizar un bucle while para seguir pidiendo números hasta que el usuario ingrese 0
while num != 0:
    suma += num  # Sumar el número actual a la suma total
    num = int(input("Ingrese otro número entero (0 para salir): "))  # Pedir otro número
# Imprimir el total acumulado 
print("El total acumulado es:", suma)
