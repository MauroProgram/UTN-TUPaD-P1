'''
Crea una funcion que reciba un numero entero positivo en decimal y devuelva su represenrtacion en binario como cadena de texto.
'''
#Dividimos el numero por 2, tomamos el resto y repetimos con el cociente
def decimal_a_binario(numero):
    if numero == 0:
        return "0"
    elif numero == 1:
        return "1"
    else:
        return decimal_a_binario(numero // 2) + str(numero % 2)

#Validacion de numero, usada en ejercicios anteriores
def validar_numero(numero):
    while numero <= 0:
        print("ERROR. El numero no puede ser negativo")
        numero = int(input("Ingrese un numero entero positivo: "))
    else:
        return decimal_a_binario(numero)


#Programa principal
num = int(input("Ingresa un numero entero positivo: "))
validar_numero(num)
print(f"El numero {num} convertido a decimal es: {decimal_a_binario(num)}")

