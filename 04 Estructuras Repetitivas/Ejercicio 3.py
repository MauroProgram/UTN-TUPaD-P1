'''
3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores
dados por el usuario, excluyendo esos dos valores.

'''

num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
# Asegurarse de que num1 sea menor que num2
if num1 > num2:
    num1, num2 = num2, num1
# Inicializar la variable suma
suma = 0
# Utilizar un bucle for para iterar desde num1 + 1 hasta num2 - 1
for i in range(num1 + 1, num2):
    suma += i  # Sumar el número actual a la suma total    
# Imprimir el resultado
print("La suma de los números enteros entre", num1, "y", num2, "es:", suma)
