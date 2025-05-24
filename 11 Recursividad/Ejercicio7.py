'''
Calcula el total de bloques en una piramide con n bloques en la base, n -1 en el siguiente nivel, hasta 1
'''

def contar_bloques(n):
    if n == 1:
        return 1
    else:
        return n + contar_bloques(n - 1)
def validar_numero(numero):
    if numero < 1:
        print("ERROR. El número debe ser un entero positivo mayor o igual a 1.")
    else:
        total_bloques = contar_bloques(numero)
        print(f"El total de bloques en la pirámide con {numero} bloques en la base es: {total_bloques}")

# Programa principal
n = int(input("Ingrese el número de bloques en la base de la pirámide: "))
validar_numero(n)
contar_bloques(n)