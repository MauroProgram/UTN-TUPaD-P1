'''
2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
dígitos que contiene

'''

num = int(input("Ingrese un número entero: "))
# Convertir el número a cadena para contar los dígitos
num_str = str(num)
# Contar la cantidad de dígitos utilizando la función len()
num_digitos = len(num_str)
# Imprimir la cantidad de dígitos
print("La cantidad de dígitos en el número", num, "es:", num_digitos)
