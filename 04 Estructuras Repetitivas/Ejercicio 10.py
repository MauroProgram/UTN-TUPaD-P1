'''
10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.

'''
# Solicita al usuario que ingrese un número entero y lo convierte a entero.
numero = int(input("Ingrese un número entero: "))

# Convierte el número a su valor absoluto para manejar negativos y luego a cadena para procesar dígitos.
numero_str = str(abs(numero))

# Invierte la cadena de dígitos usando slicing.
numero_invertido = numero_str[::-1]

# Convierte la cadena invertida de vuelta a entero.
resultado = int(numero_invertido)

# Si el número original era negativo, aplica el signo negativo al resultado.
if numero < 0:
    resultado = -resultado

# Muestra el número con los dígitos invertidos.
print("El número invertido es:", resultado)