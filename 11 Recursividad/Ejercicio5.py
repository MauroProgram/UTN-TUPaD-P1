'''
Implementa una función recursiva es_palindromo(palabra) que devuelva True si la palabra es un palíndromo, False si no.
'''
#Transoformamos a minusculas y reemplazos posibles espacios
def en_minusculas(palabra):
    palabra = palabra.lower().replace("","")
def es_palindromo(palabra):
    if len(palabra) <=1:
        return True
    else:
        if palabra [0] ==palabra[-1]:
            return es_palindromo(palabra[1:-1])
        else:
            return False
#Programa principal
palabra_usuario = input("Ingrese una unica palabra para ver si es palindromo o no: ")
resultado = es_palindromo(palabra_usuario)
if resultado:
    print(f"¡Sí! '{palabra_usuario}' es un palíndromo.")
else:
    print(f"No, '{palabra_usuario}' no es un palíndromo.")