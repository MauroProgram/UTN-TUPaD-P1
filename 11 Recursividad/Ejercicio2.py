'''
Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición indicada. Posteriormente, muestra la serie completa hasta la posición que el usuario especifique.
'''
#Calcular el valor de la serie de finobacci segun el parametro
def finobacci_recursiva(posicion):
    if posicion == 0:
        return 0
    elif posicion == 1:
        return 1
    else:
        return finobacci_recursiva(posicion -1) + finobacci_recursiva(posicion-2)
#Muestra el resultado  de la serie de finobacci en la posicion:
def mostrar_serie(numero_limite):
    print(f"\nSerie de finobacci hasta la posicion: {numero_limite}")
    for i in range (1, finobacci_recursiva(posicion) +1):
        print(f"El valor de finobacci en la posicion {i} es: {finobacci_recursiva(i)}")
#Pequenia validacion:
def validar_numero(numero):
    while numero < 0:
        print("ERROR. El numero no puede ser negativo")
    else:
        return finobacci_recursiva(posicion)
#Programa principal
posicion = int(input("Ingresa una posicion para comenzar la serie de finobacci: "))
validar_numero(posicion)
finobacci_recursiva(posicion)
mostrar_serie(posicion)
