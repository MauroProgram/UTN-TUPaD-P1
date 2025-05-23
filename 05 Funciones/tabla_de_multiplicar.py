#Funciones
def tabla_de_multiplicar(numero):
    for i in range(11):
        print(numero * i)
#Programa Principal
numero = int(input("Por favor, ingrese un numero:"))
calcular = tabla_de_multiplicar(numero)
