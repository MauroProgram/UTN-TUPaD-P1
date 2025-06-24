'''
5) Solicita al usuario una frase e imprime:
• Las palabras únicas (usando un set).
• Un diccionario con la cantidad de veces que aparece cada palabra.

'''

frase = input("Ingrese una frase: ")

# Palabras únicas
palabras = set(frase.split())
print("Palabras únicas:", palabras)

# Contar ocurrencias
contador = {}
for palabra in frase.split():
    contador[palabra] = contador.get(palabra, 0) + 1

print("Cantidad de veces que aparece cada palabra:", contador)

