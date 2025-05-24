'''
Escribe una función recursiva suma_digitos(n) que sume los dígitos de un número sin convertirlo a string.
'''

def suma_digitos(num):
    if num < 10:
        return num
    else:
        ultimo_digito = num % 10
        resto_del_digito = num // 10
    return ultimo_digito + suma_digitos(resto_del_digito)

def validar_num(num):
    if num <=0: 
        print("ERROR. Se esperaba un numero entero positivo.")
    else:
        print(f"La suma de los digitos de {num} es: {suma_digitos(num)}")

num = int(input("Ingresa un numero: "))
suma_de_los_digitos = validar_num(num)