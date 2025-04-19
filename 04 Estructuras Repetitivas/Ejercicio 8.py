# Programa para contar cuántos números enteros son pares, impares, positivos y negativos.

# Inicializar contadores para rastrear las categorías de los números ingresados.
cont_pares = 0
cont_impares = 0
cont_positivos = 0
cont_negativos = 0

# Define la cantidad de números a ingresar (100 para el enunciado, 5 para pruebas).
cantidad_numeros = 5  # Cambiar a 100 para cumplir el enunciado completo.

# Usa un bucle para solicitar los números al usuario.
for i in range(cantidad_numeros):
    # Pide un número entero y lo convierte de texto a entero.
    num = int(input("Ingrese un número entero: "))
    
    # Verifica si el número es par (divisible por 2 sin resto).
    if num % 2 == 0:
        cont_pares += 1  # Incrementa el contador de pares.
    else:
        cont_impares += 1  # Incrementa el contador de impares.
    
    # Verifica si el número es positivo o negativo.
    if num > 0:
        cont_positivos += 1  # Incrementa el contador de positivos.
    elif num < 0:
        cont_negativos += 1  # Incrementa el contador de negativos.

# Muestra los resultados finales de los contadores.
print("Cantidad de números pares:", cont_pares)
print("Cantidad de números impares:", cont_impares)
print("Cantidad de números positivos:", cont_positivos)
print("Cantidad de números negativos:", cont_negativos)