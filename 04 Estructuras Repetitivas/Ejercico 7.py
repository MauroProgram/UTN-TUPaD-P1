'''
7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
número entero positivo indicado por el usuario.
'''
num = int(input("Ingrese un número entero positivo: "))
# Inicializar la variable suma
suma = 0
# Utilizar un bucle for para iterar desde 0 hasta el número ingresado
# (incluyendo el número ingresado)
for i in range(num + 1):
    suma += i  # Sumar el número actual a la suma total 
# Imprimir el resultado
print("La suma de los números enteros entre 0 y", num, "es:", suma)

