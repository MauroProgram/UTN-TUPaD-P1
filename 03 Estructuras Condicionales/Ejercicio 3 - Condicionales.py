# Programa para verificar si un número ingresado es par.

# Solicita al usuario un número y lo convierte a entero.
num = int(input("Por favor, ingrese un número par: "))

# Verifica si el número es par usando el operador módulo.
if num % 2 == 0:
    print(f"¡Correcto! {num} es un número par.")
else:
    print(f"Error: {num} no es un número par. Por favor, ingrese un número par.")