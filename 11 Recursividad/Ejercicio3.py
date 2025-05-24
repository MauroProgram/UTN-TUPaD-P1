'''
Crea una función recursiva que calcule la potencia de un número base elevado a un exponente, utilizando la fórmula <math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><msup><mi>n</mi><mi>m</mi></msup><mo>=</mo><mi>n</mi><mo>×</mo><msup><mi>n</mi><mrow><mo stretchy="false">(</mo><mi>m</mi><mo>−</mo><mn>1</mn><mo stretchy="false">)</mo></mrow></msup></mrow><annotation encoding="application/x-tex"> n^m = n \times n^{(m-1)} </annotation></semantics></math>.
'''
#Funcion para sacar la potencia de un numero
def potencia_de_un_numero(numero,exponente):
    if exponente == 0 :
        return 1
    else:
        return numero * potencia_de_un_numero (numero,exponente -1)
#Validacion para numeros negativos
def validar_numero(numero1,numero2):
    if numero1 <=0 or numero2 <= 0:
        print("ERROR. Se necesita un numero entero positivo distinto de 0")
    else:
        return potencia_de_un_numero(numero1,numero2)

#Programa principal
numero = int(input("Ingresa un numero para sacar su potencia: "))
exponente = int(input("Ingresa el exponente deseado: "))
validar_numero(numero,exponente)
print(potencia_de_un_numero(numero,exponente))