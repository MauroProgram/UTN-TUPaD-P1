'''
5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
programa debe mostrar cuántos intentos fueron necesarios para acertar el número.

'''
import random
# Generar un número aleatorio entre 0 y 9
numero_aleatorio = random.randint(0, 9)
# Inicializar el contador de intentos
intentos = 0
# Inicializar la variable para almacenar la suposición del usuario
suponiendo = -1  # Un valor que no es válido para el rango de números           
# Utilizar un bucle while para seguir pidiendo números hasta que el usuario adivine el correcto
while suponiendo != numero_aleatorio:
    suponiendo = int(input("Adivina el número entre 0 y 9: "))  # Pedir al usuario que adivine
    intentos += 1  # Incrementar el contador de intentos
# Imprimir el número de intentos necesarios para adivinar el número
print("¡Felicidades! Adivinaste el número", numero_aleatorio, "en", intentos, "intentos.")

