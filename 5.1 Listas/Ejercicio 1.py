'''
Crear una lista con los números del 1 al 100 que sean múltiplos de 4. Utilizar la función range.
'''

numeros = list(range(1,101))
numeros = [i for i in numeros if i % 4 == 0]
print(numeros) 