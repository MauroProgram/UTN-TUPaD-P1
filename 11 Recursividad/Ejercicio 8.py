'''Funcion recursiva que cuente cuantas veces aparece un digito en un numero'''

def contar_digito(numero, digito):
    if numero == 0:
        return 0
    elif numero < 10:
        if numero == digito:
            return 1
        else:
            return 0
    else:
        if (numero % 10) == digito:
            return 1 + contar_digito(numero // 10, digito)
        else:
            return contar_digito(numero // 10, digito)
def validar_numero(numero, digito):
    if numero < 0 or digito < 0 or digito > 9:
        print("ERROR. El numero debe ser entero positivo y el digito debe estar entre 0 y 9.")  
    else:
        cantidad = contar_digito(numero, digito)
        print(f"El digito {digito} aparece {cantidad} veces en el numero {numero}.")
#Programa principal
numero = int(input("Ingrese un numero entero positivo: "))
digito = int(input("Ingrese el digito que desea contar: ")) 
validar_numero(numero, digito)
contar_digito(numero, digito)